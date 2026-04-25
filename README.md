# TaxGPT India 🇮🇳 (Local RAG System)

A production-ready, fully local Retrieval-Augmented Generation (RAG) pipeline designed specifically for Indian Tax Compliance (Income Tax Act, CGST, IGST, ITR Rules). It is built to run 100% locally without any external API keys, ensuring complete data privacy for sensitive financial queries.

## ✨ Features
- **Legal-Aware Chunking**: Intelligently splits massive legal PDFs by Sections, Rules, and Chapters to preserve context.
- **Source Citations**: The LLM explicitly cites the exact source document and page number for every fact `[Source 1 | income_tax_act.pdf (Page 45)]`.
- **Query Transformation**: Intercepts user queries and rewrites them into optimized vector search queries.
- **Microservice Architecture**: Decoupled FastAPI backend and Streamlit frontend.
- **Local AI Stack**: Powered by Qwen 2.5 3B (GGUF) and `all-MiniLM-L6-v2` via FAISS.
- **Automated Evaluation**: Includes an evaluation pipeline to measure *Semantic Similarity*, *ROUGE-L*, and *Grounded Precision* against a golden dataset of tax queries.

## 🏗️ Architecture

1. **Ingestion (`ingest_data.py`)**: Reads government tax PDFs, performs legal-aware chunking, embeds using SentenceTransformers, and stores in a FAISS index with metadata.
2. **Backend (`api.py`)**: A FastAPI server with lifespan management and health checks that serves the `/chat` endpoint.
3. **Frontend (`app.py`)**: A professional Streamlit web interface tailored for tax queries.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Place your local GGUF model in the `MODEL/` directory (e.g., `qwen2.5-3b-instruct-q4_k_m.gguf`).
- Download the official Indian tax laws (Income Tax Act 1961, CGST Act, ITR Instructions) as PDFs and place them in the `data/TAX/` directory.

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/indian-tax-rag.git
cd indian-tax-rag

# Install dependencies
pip install -r requirements.txt
```

### 1. Ingest Tax Data
Run the ingestion script to process the PDFs and build the FAISS index:
```bash
python ingest_data.py
```

### 2. Start the Application
Run the microservices in two separate terminals.

**Terminal 1 (Backend):**
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

**Terminal 2 (Frontend):**
```bash
streamlit run app.py
```

## 🐳 Docker Deployment
This project is fully containerized.
```bash
docker build -t taxgpt-india .
docker run -p 8000:8000 -p 8501:8501 taxgpt-india
```

## 📊 Evaluation
To run the automated evaluation pipeline against the 25-question tax golden dataset:
```bash
python scripts/evaluate.py
```
This will output an `evaluation_results.md` report detailing the performance of the system using ROUGE-L and Semantic Similarity metrics.
