FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Streamlit and FastAPI ports
EXPOSE 8501
EXPOSE 8000

# Make start script executable
RUN chmod +x start.sh

CMD ["./start.sh"]
