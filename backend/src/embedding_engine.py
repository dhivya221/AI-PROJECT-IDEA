"""
Embedding Engine - Converts text to embeddings for vector search
"""
from typing import List
import google.generativeai as genai
from src.config import GOOGLE_API_KEY

class EmbeddingEngine:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = "models/embedding-001"
    
    def embed_text(self, text: str) -> List[float]:
        """Convert text to embedding vector"""
        response = genai.embed_content(
            model=self.model,
            content=text,
            task_type="retrieval_document"
        )
        return response['embedding']
    
    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Convert multiple texts to embeddings"""
        response = genai.embed_content(
            model=self.model,
            content=texts,
            task_type="retrieval_document"
        )
        return response['embedding']

# Singleton instance
_embedding_engine = None

def get_embedding_engine():
    global _embedding_engine
    if _embedding_engine is None:
        _embedding_engine = EmbeddingEngine()
    return _embedding_engine
