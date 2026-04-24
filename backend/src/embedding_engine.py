"""
Embedding Engine - Converts text to embeddings for vector search
"""
from typing import List
import openai
from src.config import OPENAI_API_KEY

class EmbeddingEngine:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = "text-embedding-3-small"
    
    def embed_text(self, text: str) -> List[float]:
        """Convert text to embedding vector"""
        response = openai.Embedding.create(
            input=text,
            model=self.model
        )
        return response['data'][0]['embedding']
    
    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Convert multiple texts to embeddings"""
        response = openai.Embedding.create(
            input=texts,
            model=self.model
        )
        # Sort by index to maintain order
        return [item['embedding'] for item in sorted(response['data'], key=lambda x: x['index'])]

# Singleton instance
_embedding_engine = None

def get_embedding_engine():
    global _embedding_engine
    if _embedding_engine is None:
        _embedding_engine = EmbeddingEngine()
    return _embedding_engine
