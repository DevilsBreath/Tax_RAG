import json
import faiss
import logging
from sentence_transformers import SentenceTransformer
from src import config
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class VectorStore:
    def __init__(self):
        logger.info(f"Loading embedding model from {config.EMBED_MODEL_DIR}")
        self.embedder = SentenceTransformer(str(config.EMBED_MODEL_DIR), local_files_only=True)
        self.index = None
        self.chunks = []

    def build_index(self, chunks: List[Dict[str, Any]]):
        self.chunks = chunks
        logger.info("Encoding chunks...")
        texts = [c["text"] for c in chunks]
        embeddings = self.embedder.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        embeddings = embeddings.astype("float32")
        
        logger.info("Building FAISS index...")
        self.index = faiss.IndexFlatIP(embeddings.shape[1])
        self.index.add(embeddings)

    def save(self):
        config.VECTOR_DIR.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self.index, str(config.INDEX_PATH))
        config.CHUNKS_PATH.write_text(json.dumps(self.chunks, indent=2), encoding="utf-8")
        logger.info(f"Saved FAISS index to: {config.INDEX_PATH}")
        logger.info(f"Saved chunks metadata to: {config.CHUNKS_PATH}")

    def load(self):
        if not config.INDEX_PATH.exists() or not config.CHUNKS_PATH.exists():
            raise FileNotFoundError("Index files missing. Run ingest first.")
        
        self.index = faiss.read_index(str(config.INDEX_PATH))
        self.chunks = json.loads(config.CHUNKS_PATH.read_text(encoding="utf-8"))
        logger.info(f"Loaded FAISS index with {len(self.chunks)} chunks.")

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        if self.index is None:
            self.load()
            
        q_vec = self.embedder.encode([query], convert_to_numpy=True, normalize_embeddings=True).astype("float32")
        scores, ids = self.index.search(q_vec, top_k)
        
        hits = []
        for rank, (doc_id, score) in enumerate(zip(ids[0], scores[0]), start=1):
            chunk_data = self.chunks[int(doc_id)]
            if isinstance(chunk_data, str):
                text, metadata = chunk_data, {}
            else:
                text, metadata = chunk_data["text"], chunk_data.get("metadata", {})
            hits.append({
                "rank": rank,
                "score": float(score),
                "text": text,
                "metadata": metadata
            })
        return hits
