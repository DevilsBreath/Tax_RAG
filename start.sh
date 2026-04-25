#!/bin/bash

# Start FastAPI backend in the background
uvicorn api:app --host 0.0.0.0 --port 8000 &

# Wait a few seconds for the API and models to load
sleep 5

# Start Streamlit frontend
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
