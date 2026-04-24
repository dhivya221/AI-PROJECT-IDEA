"""
Vector Search - RAG retrieval using Pinecone
"""
from typing import List, Dict, Any
from pinecone import Pinecone
from src.config import PINECONE_API_KEY, PINECONE_INDEX_NAME, PINECONE_DIMENSION
from src.embedding_engine import get_embedding_engine

class VectorSearch:
    def __init__(self):
        self.mock_mode = (PINECONE_API_KEY == "your_pinecone_key_here" or not PINECONE_API_KEY)
        if not self.mock_mode:
            try:
                self.pc = Pinecone(api_key=PINECONE_API_KEY)
                self.index = self.pc.Index(PINECONE_INDEX_NAME)
            except Exception as e:
                print(f"Failed to initialize Pinecone, falling back to mock mode: {e}")
                self.mock_mode = True
        
        self.embedding_engine = get_embedding_engine()
        self.mock_storage = []
    
    def index_document(self, doc_id: str, text: str, metadata: Dict[str, Any] = None):
        """Index a document in Pinecone"""
        if self.mock_mode:
            print(f"[MOCK RAG] Indexing document {doc_id}")
            self.mock_storage.append({
                "id": doc_id,
                "text": text,
                "metadata": metadata or {}
            })
            return
            
        embedding = self.embedding_engine.embed_text(text)
        self.index.upsert([(doc_id, embedding, {"text": text, **(metadata or {})})])
    
    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Search for similar documents"""
        if self.mock_mode:
            print(f"[MOCK RAG] Searching for {query}")
            # Mock return of recent items if any
            return [
                {
                    "id": doc["id"],
                    "score": 0.95,
                    "metadata": doc["metadata"]
                }
                for doc in self.mock_storage[:top_k]
            ]
            
        query_embedding = self.embedding_engine.embed_text(query)
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )
        
        return [
            {
                "id": match["id"],
                "score": match["score"],
                "metadata": match.get("metadata", {})
            }
            for match in results["matches"]
        ]
    
    def delete_document(self, doc_id: str):
        """Delete a document from index"""
        if self.mock_mode:
            self.mock_storage = [d for d in self.mock_storage if d["id"] != doc_id]
            return
        self.index.delete(ids=[doc_id])
    
    def clear_index(self):
        """Clear all documents from index"""
        if self.mock_mode:
            self.mock_storage = []
            return
        self.index.delete(delete_all=True)

# Singleton instance
_vector_search = None

def get_vector_search():
    global _vector_search
    if _vector_search is None:
        _vector_search = VectorSearch()
    return _vector_search
