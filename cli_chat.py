from src.rag_pipeline import RAGPipeline

def main():
    print("Initializing RAG Pipeline...")
    try:
        pipeline = RAGPipeline()
    except Exception as e:
        print(f"Error initializing pipeline: {e}")
        print("Have you run ingest_data.py yet?")
        return

    print("\n" + "="*50)
    print("Local RAG CLI (type 'exit' to quit)")
    print("="*50)
    
    while True:
        question = input("\nQ: ")
        if question.lower() in ['exit', 'quit']:
            break
            
        print("Thinking...")
        answer, evidence = pipeline.answer_question(question)
        
        print(f"\nA: {answer}\n")
        print("Sources:")
        for item in evidence:
            print(f"  [{item['rank']}] (score: {item['score']:.4f}) {item['text'][:100]}...")

if __name__ == "__main__":
    main()
