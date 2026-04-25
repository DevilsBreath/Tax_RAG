import numpy as np
import logging
from sentence_transformers import SentenceTransformer
from rouge_score import rouge_scorer
from src import config

logger = logging.getLogger(__name__)

class Evaluator:
    def __init__(self):
        logger.info("Loading embedding model for evaluation...")
        self.embedder = SentenceTransformer(str(config.EMBED_MODEL_DIR), local_files_only=True)
        self.rouge = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

    def calculate_semantic_similarity(self, generated_answer: str, expected_answer: str) -> float:
        """Calculates cosine similarity between generated and expected answers."""
        vecs = self.embedder.encode([generated_answer, expected_answer], convert_to_numpy=True, normalize_embeddings=True)
        return float(np.dot(vecs[0], vecs[1]))

    def calculate_rouge_l(self, generated_answer: str, expected_answer: str) -> float:
        """Calculates ROUGE-L F1 score."""
        scores = self.rouge.score(expected_answer, generated_answer)
        return scores['rougeL'].fmeasure

    def calculate_grounded_precision(self, answer: str, context_chunks: list) -> float:
        """Naive grounded precision based on keyword overlap."""
        answer_words = set(answer.lower().split())
        if not answer_words:
            return 0.0
            
        context_text = " ".join([chunk['text'] for chunk in context_chunks]).lower()
        context_words = set(context_text.split())
        
        overlap = answer_words.intersection(context_words)
        return len(overlap) / len(answer_words)

    def evaluate_response(self, question: str, expected_answer: str, generated_answer: str, context_chunks: list) -> dict:
        semantic_sim = self.calculate_semantic_similarity(generated_answer, expected_answer)
        rouge_l = self.calculate_rouge_l(generated_answer, expected_answer)
        precision = self.calculate_grounded_precision(generated_answer, context_chunks)
        
        # Simple composite score
        composite = (semantic_sim * 0.5) + (rouge_l * 0.3) + (precision * 0.2)
        
        return {
            "semantic_similarity": round(semantic_sim, 4),
            "rouge_l": round(rouge_l, 4),
            "grounded_precision": round(precision, 4),
            "composite_score": round(composite, 4)
        }
