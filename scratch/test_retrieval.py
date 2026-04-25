import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.vector_store import VectorStore

vs = VectorStore()
retrieved = vs.retrieve("standard deduction limit for salaried employees under the new tax regime (Section 115BAC) for FY 2025-26", top_k=5)
for i, r in enumerate(retrieved):
    print(f"--- Chunk {i} | Score: {r['score']} ---")
    print(r['text'][:500])
    print()
