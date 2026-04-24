"""
Application entry point
"""
import sys
import logging
from src.app import app
from src.config import PORT, HOST

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    import uvicorn
    
    print(f"Starting AI Project Idea Generator API on {HOST}:{PORT}")
    print("Documentation available at http://localhost:3000/docs")
    
    uvicorn.run(
        app,
        host=HOST,
        port=PORT,
        log_level="info"
    )
