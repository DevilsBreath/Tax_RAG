import sys
from pathlib import Path
import logging
# Add parent dir to path so we can import src
sys.path.append(str(Path(__file__).parent.parent))

import json
from src.rag_pipeline import RAGPipeline
from src.evaluator import Evaluator
from src import config

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def main():
    eval_file = config.EVAL_DATA_DIR / "eval_dataset.json"
    if not eval_file.exists():
        logger.error(f"Evaluation dataset not found at {eval_file}")
        return

    with open(eval_file, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    logger.info("Initializing Tax RAG Pipeline and Evaluator...")
    pipeline = RAGPipeline()
    evaluator = Evaluator()

    results = []
    
    logger.info("\nStarting Evaluation...")
    for idx, item in enumerate(dataset):
        question = item["question"]
        expected = item["expected_answer"]
        
        logger.info(f"\n[{idx+1}/{len(dataset)}] Evaluating: {question}")
        answer, context = pipeline.answer_question(question, top_k=4)
        
        metrics = evaluator.evaluate_response(question, expected, answer, context)
        
        results.append({
            "question": question,
            "expected_answer": expected,
            "generated_answer": answer,
            "metrics": metrics
        })
        
        logger.info(f"  Similarity: {metrics['semantic_similarity']}")
        logger.info(f"  ROUGE-L: {metrics['rouge_l']}")
        logger.info(f"  Precision: {metrics['grounded_precision']}")

    # Save results
    report_path = config.PROJECT_ROOT / "evaluation_results_2.md"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# TaxGPT India RAG Pipeline Evaluation Results\n\n")
        f.write("## Overall Metrics\n")
        
        avg_sim = sum(r["metrics"]["semantic_similarity"] for r in results) / len(results)
        avg_rouge = sum(r["metrics"]["rouge_l"] for r in results) / len(results)
        avg_prec = sum(r["metrics"]["grounded_precision"] for r in results) / len(results)
        
        f.write(f"- **Average Semantic Similarity:** {avg_sim:.4f}\n")
        f.write(f"- **Average ROUGE-L:** {avg_rouge:.4f}\n")
        f.write(f"- **Average Grounded Precision:** {avg_prec:.4f}\n\n")
        
        f.write("## Detailed Breakdown\n")
        for idx, r in enumerate(results):
            f.write(f"### Q{idx+1}: {r['question']}\n")
            f.write(f"- **Expected:** {r['expected_answer']}\n")
            f.write(f"- **Generated:** {r['generated_answer']}\n")
            f.write(f"- **Similarity:** {r['metrics']['semantic_similarity']} | **ROUGE-L:** {r['metrics']['rouge_l']} | **Precision:** {r['metrics']['grounded_precision']}\n\n")
            
    logger.info(f"\nEvaluation complete! Report saved to {report_path}")

if __name__ == "__main__":
    main()
