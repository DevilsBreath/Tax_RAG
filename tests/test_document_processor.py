import pytest
from src.document_processor import chunk_text

def test_chunk_text_legal_markers():
    pages_data = [
        {
            "text": "Section 1. This is the first section.\n\nSection 2. This is the second section.",
            "source": "test.pdf",
            "page": 1
        }
    ]
    
    chunks = chunk_text(pages_data, chunk_size=100, overlap=0)
    
    # It should split around 'Section 2'
    assert len(chunks) == 2
    assert "Section 1" in chunks[0]["text"]
    assert "Section 2" in chunks[1]["text"]
    assert chunks[0]["metadata"]["source"] == "test.pdf"

def test_chunk_text_overlap():
    pages_data = [
        {
            "text": "This is a very long text that needs to be split because it is larger than the chunk size.",
            "source": "test.pdf",
            "page": 1
        }
    ]
    
    # Small chunk size to force splitting by sentence or words
    chunks = chunk_text(pages_data, chunk_size=40, overlap=2)
    
    assert len(chunks) > 1
    # Check if metadata is preserved
    for chunk in chunks:
        assert chunk["metadata"]["source"] == "test.pdf"
