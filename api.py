from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from contextlib import asynccontextmanager
import logging
from src.rag_pipeline import RAGPipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize pipeline globally
pipeline = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global pipeline
    logger.info("Initializing Tax RAG Pipeline...")
    try:
        pipeline = RAGPipeline()
        logger.info("Pipeline initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize pipeline: {e}")
    yield
    logger.info("Shutting down API...")

app = FastAPI(title="TaxGPT India API", version="1.0", lifespan=lifespan)

class QueryRequest(BaseModel):
    question: str
    top_k: int = 4

class QueryResponse(BaseModel):
    answer: str
    evidence: List[Dict[str, Any]]

@app.get("/health")
def health_check():
    if pipeline:
        return {"status": "healthy", "pipeline_initialized": True}
    return {"status": "unhealthy", "pipeline_initialized": False}

@app.post("/chat", response_model=QueryResponse)
def chat(request: QueryRequest):
    if not pipeline:
        raise HTTPException(status_code=503, detail="Pipeline not initialized. Did you run ingest_data.py?")
    
    try:
        answer, evidence = pipeline.answer_question(request.question, top_k=request.top_k)
        return {"answer": answer, "evidence": evidence}
    except Exception as e:
        detail = str(e).strip() or f"{type(e).__name__}: {repr(e)}"
        logger.exception("Error during chat")
        raise HTTPException(status_code=500, detail=detail)
