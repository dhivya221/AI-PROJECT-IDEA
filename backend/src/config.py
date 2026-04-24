import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_MODEL = "gemini-1.5-flash"

# Pinecone Configuration
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "project-ideas-index")
PINECONE_DIMENSION = 768  # Google embedding dimension

# Server Configuration
PORT = int(os.getenv("PORT", 3000))
HOST = "127.0.0.1"

# Validation
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not set in environment variables")
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY not set in environment variables")

print("API KEY:", GOOGLE_API_KEY[:5] + "...")