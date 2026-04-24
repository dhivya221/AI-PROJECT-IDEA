"""
FastAPI application - REST API for the idea generator
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

from src.models import DomainInput, ProjectEvaluation
from src.orchestrator import get_orchestrator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Project Idea Generator",
    description="Generate and evaluate AI project ideas based on domain input",
    version="1.0.0"
)

# Add CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "AI Project Idea Generator API is running"}

@app.post("/evaluate", response_model=ProjectEvaluation)
async def evaluate_domain(input_data: DomainInput):
    """
    Evaluate a domain and generate project ideas with scoring
    
    Args:
        input_data: Domain input with optional context
        
    Returns:
        ProjectEvaluation: Complete evaluation with ideas, scores, and recommendations
    """
    try:
        orchestrator = get_orchestrator()
        result = orchestrator.evaluate(
            domain=input_data.domain,
            context=input_data.context,
            num_ideas=5
        )
        return result
    except Exception as e:
        logger.error(f"Evaluation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "idea-generator"}

if __name__ == "__main__":
    import uvicorn
    from src.config import PORT, HOST
    
    uvicorn.run(
        app,
        host=HOST,
        port=PORT,
        log_level="info"
    )
