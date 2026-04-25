import sys
import logging
from src import config
from src.document_processor import read_text_from_pdfs, chunk_text
from src.vector_store import VectorStore

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting data ingestion...")
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)
    pdf_files = sorted(config.DATA_DIR.glob("*.pdf"))
    
    pages_data = []
    if pdf_files:
        logger.info(f"Found {len(pdf_files)} PDF files.")
        pages_data = read_text_from_pdfs(pdf_files)
    
    if not pages_data:
        # Fallback to plain text if no PDFs
        if config.KB_PATH.exists():
            text = config.KB_PATH.read_text(encoding="utf-8")
            pages_data = [{"text": text, "source": "knowledge_base.txt", "page": 1}]
            logger.info("Using fallback knowledge base.")
        else:
            logger.error("No PDFs or text found in data/TAX. Exiting.")
            sys.exit(1)

    logger.info("Chunking text...")
    chunks = chunk_text(pages_data)
    logger.info(f"Created {len(chunks)} chunks.")
    
    vs = VectorStore()
    vs.build_index(chunks)
    vs.save()
    logger.info("Ingestion complete.")

if __name__ == "__main__":
    main()
