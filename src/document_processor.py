import re
import logging
from pypdf import PdfReader
from src import config
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

def read_text_from_pdfs(pdf_paths) -> List[Dict[str, Any]]:
    """Reads PDFs and returns a list of pages with metadata."""
    pages_data = []
    for pdf_path in pdf_paths:
        try:
            reader = PdfReader(str(pdf_path))
            for i, page in enumerate(reader.pages):
                page_text = page.extract_text() or ""
                page_text = page_text.strip()
                if page_text:
                    pages_data.append({
                        "text": page_text,
                        "source": pdf_path.name,
                        "page": i + 1
                    })
            logger.info(f"Loaded {pdf_path.name}: {len(reader.pages)} pages")
        except Exception as exc:
            logger.error(f"Failed to read {pdf_path.name}: {exc}")
    return pages_data

def chunk_text(pages_data: List[Dict[str, Any]], chunk_size: int = config.CHUNK_SIZE, overlap: int = config.CHUNK_OVERLAP) -> List[Dict[str, Any]]:
    """Splits text into chunks, respecting legal sections and applying overlap."""
    chunks = []
    
    for page_data in pages_data:
        raw_text = page_data["text"]
        source = page_data["source"]
        page_num = page_data["page"]
        
        # Split by legal markers (Section, Rule, Chapter) or paragraphs
        # This regex looks for "Section X", "Rule Y", "Chapter Z" or double newlines
        parts = re.split(r'(?i)(\n\s*(?:Section|Rule|Chapter|Article)\s+[\dIVX]+|\n\s*\n)', raw_text)
        
        current_chunk_text = ""
        
        for part in parts:
            part = re.sub(r"\s+", " ", part).strip()
            if not part:
                continue
                
            if len(current_chunk_text) + len(part) <= chunk_size:
                current_chunk_text += ("\n\n" if current_chunk_text else "") + part
            else:
                if current_chunk_text:
                    chunks.append({
                        "text": current_chunk_text,
                        "metadata": {"source": source, "page": page_num}
                    })
                
                # Apply overlap if we already had some text
                if current_chunk_text and overlap > 0:
                    overlap_text = current_chunk_text[-overlap:]
                    if " " in overlap_text and len(current_chunk_text) > overlap:
                        overlap_text = overlap_text.split(" ", 1)[-1]
                    current_chunk_text = overlap_text + "\n\n" + part
                else:
                    current_chunk_text = part
                    
                # If a single part is still larger than chunk_size, split by sentences
                while len(current_chunk_text) > chunk_size:
                    sentences = re.split(r'(?<=[.!?]) +', current_chunk_text)
                    sub_chunk = ""
                    remaining_text = ""
                    
                    for i, sent in enumerate(sentences):
                        if len(sub_chunk) + len(sent) <= chunk_size:
                            sub_chunk += (" " if sub_chunk else "") + sent
                        else:
                            if not sub_chunk:
                                # A single sentence is longer than chunk_size, split by characters
                                sub_chunk = sent[:chunk_size]
                                remaining_sentences = sentences[i+1:]
                                if remaining_sentences:
                                    remaining_text = sent[chunk_size:] + " " + " ".join(remaining_sentences)
                                else:
                                    remaining_text = sent[chunk_size:]
                            else:
                                remaining_text = " ".join(sentences[i:])
                            break
                    
                    if sub_chunk:
                        chunks.append({
                            "text": sub_chunk.strip(),
                            "metadata": {"source": source, "page": page_num}
                        })
                    current_chunk_text = remaining_text.strip()
                    
        if current_chunk_text:
            chunks.append({
                "text": current_chunk_text,
                "metadata": {"source": source, "page": page_num}
            })
            
    return chunks
