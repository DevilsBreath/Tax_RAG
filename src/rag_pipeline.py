import logging
from src.vector_store import VectorStore
from src.llm_engine import LLMEngine

logger = logging.getLogger(__name__)

class RAGPipeline:
    def __init__(self):
        self.vector_store = VectorStore()
        self.llm = LLMEngine()

    def transform_query(self, question: str) -> str:
        messages = [
            {"role": "system", "content": "You are a search query generator for Indian Tax Laws. Your task is to rewrite the user's question into an optimized search query for a vector database. Extract key tax terms (e.g., sections, regimes, deductions, GST). Only return the search query, nothing else."},
            {"role": "user", "content": f"Question: {question}"}
        ]
        rewritten = self.llm.generate(messages, max_tokens=60, temperature=0.1)
        logger.info(f"Original Query: {question}")
        logger.info(f"Transformed Query: {rewritten}")
        if len(rewritten) > 100 or "I don't" in rewritten or not rewritten.strip():
            return question
        return rewritten

    def answer_question(self, question: str, top_k: int = 8, max_new_tokens: int = 512):
        search_query = self.transform_query(question)
        retrieved = self.vector_store.retrieve(search_query, top_k=top_k)
        
        context_parts = []
        for r in retrieved:
            meta = r.get("metadata", {})
            source_name = meta.get("source", "Unknown Document")
            page_num = meta.get("page", "?")
            context_parts.append(f"[Source {r['rank']} | {source_name} (Page {page_num})]\n{r['text']}")
            
        context_block = "\n\n".join(context_parts)

        messages = [
            {"role": "system", "content": "You are an expert Indian Chartered Accountant and Tax Advisor. Answer the user's question accurately based ONLY on the provided legal context.\nIMPORTANT INSTRUCTION: You MUST cite the sources you use in your answer by appending [Source X] at the end of the sentence where the fact is used.\nIf the context contains partial or related information, synthesize the best possible answer from it — do not refuse if relevant facts are present.\nOnly say \"I don't know based on the provided tax documents.\" if the context contains absolutely no information relevant to the question. Do not invent facts, figures, or section numbers not found in the context."},
            {"role": "user", "content": f"Context:\n{context_block}\n\nQuestion: {question}"}
        ]
        answer = self.llm.generate(messages, max_tokens=max_new_tokens)
        return answer, retrieved
