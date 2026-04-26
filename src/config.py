from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

PROJECT_ROOT = Path(__file__).parent.parent
MODEL_DIR = PROJECT_ROOT / "MODEL"
EMBED_MODEL_DIR = MODEL_DIR / "embeddings" / "bge-base-en-v1.5"
LLM_MODEL_DIR = MODEL_DIR / "gemma-4-E4B-it-UD-Q4_K_XL.gguf"
# MODEL\gemma-4-E4B-it-UD-Q4_K_XL.gguf  \MODEL\embeddings\bge-base-en-v1.5
EVAL_DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR = PROJECT_ROOT / "data" / "TAX"
VECTOR_DIR = PROJECT_ROOT / "vectorstore"

KB_PATH = DATA_DIR / "knowledge_base.txt"
EXTRACTED_PDF_TEXT_PATH = DATA_DIR / "extracted_pdf_text.txt"
INDEX_PATH = VECTOR_DIR / "faiss_index.bin"
CHUNKS_PATH = VECTOR_DIR / "chunks.json"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200