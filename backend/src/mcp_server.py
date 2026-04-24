"""
MCP Server - Model Context Protocol server implementing all tools
"""
import json
from typing import Any, Dict, List
from mcp.server import Server
from mcp.types import Tool, TextContent, ToolResult
import logging

from src.domain_analyzer import get_domain_analyzer
from src.idea_generator import get_idea_generator
from src.complexity_estimator import get_complexity_estimator
from src.tech_stack_recommender import get_tech_stack_recommender
from src.scoring_module import get_scoring_module
from src.recommendation_engine import get_recommendation_engine
from src.vector_search import get_vector_search
from src.models import DomainInput, ProjectEvaluation

logger = logging.getLogger(__name__)

class IdeaGeneratorMCPServer:
    def __init__(self):
        self.server = Server("idea-generator")
        self._register_tools()
    
    def _register_tools(self):
        """Register all MCP tools"""
        
        @self.server.call_tool()
        async def analyze_domain(domain: str, context: str = None) -> Dict[str, Any]:
            """Analyze a domain for characteristics and opportunities"""
            try:
                analyzer = get_domain_analyzer()
                result = analyzer.analyze(domain, context)
                return {"status": "success", "data": result}
            except Exception as e:
                logger.error(f"Domain analysis error: {e}")
                return {"status": "error", "error": str(e)}
        
        @self.server.call_tool()
        async def generate_ideas(domain: str, analysis: str, num_ideas: int = 5) -> Dict[str, Any]:
            """Generate project ideas based on domain analysis"""
            try:
                generator = get_idea_generator()
                ideas = generator.generate(domain, analysis, num_ideas)
                return {
                    "status": "success",
                    "data": [idea.model_dump() for idea in ideas]
                }
            except Exception as e:
                logger.error(f"Idea generation error: {e}")
                return {"status": "error", "error": str(e)}
        
        @self.server.call_tool()
        async def estimate_complexity(ideas_json: str) -> Dict[str, Any]:
            """Estimate complexity for project ideas"""
            try:
                from src.models import ProjectIdea
                ideas_data = json.loads(ideas_json)
                ideas = [ProjectIdea(**idea) for idea in ideas_data]
                
                estimator = get_complexity_estimator()
                estimations = estimator.estimate(ideas)
                return {
                    "status": "success",
                    "data": [est.model_dump() for est in estimations]
                }
            except Exception as e:
                logger.error(f"Complexity estimation error: {e}")
                return {"status": "error", "error": str(e)}
        
        @self.server.call_tool()
        async def recommend_tech_stack(ideas_json: str) -> Dict[str, Any]:
            """Recommend technology stacks for ideas"""
            try:
                from src.models import ProjectIdea
                ideas_data = json.loads(ideas_json)
                ideas = [ProjectIdea(**idea) for idea in ideas_data]
                
                recommender = get_tech_stack_recommender()
                stacks = recommender.recommend(ideas)
                return {
                    "status": "success",
                    "data": [[item.model_dump() for item in stack] for stack in stacks]
                }
            except Exception as e:
                logger.error(f"Tech stack recommendation error: {e}")
                return {"status": "error", "error": str(e)}
        
        @self.server.call_tool()
        async def score_ideas(ideas_json: str, domain: str) -> Dict[str, Any]:
            """Score ideas on feasibility, innovation, and market potential"""
            try:
                from src.models import ProjectIdea
                ideas_data = json.loads(ideas_json)
                ideas = [ProjectIdea(**idea) for idea in ideas_data]
                
                scorer = get_scoring_module()
                scores = scorer.score(ideas, domain)
                return {
                    "status": "success",
                    "data": [score.model_dump() for score in scores]
                }
            except Exception as e:
                logger.error(f"Scoring error: {e}")
                return {"status": "error", "error": str(e)}
        
        @self.server.call_tool()
        async def vector_search(query: str, top_k: int = 5) -> Dict[str, Any]:
            """Search for similar ideas using vector embeddings (RAG)"""
            try:
                vs = get_vector_search()
                results = vs.search(query, top_k)
                return {"status": "success", "data": results}
            except Exception as e:
                logger.error(f"Vector search error: {e}")
                return {"status": "error", "error": str(e)}
        
        @self.server.call_tool()
        async def get_recommendations(domain: str, ideas_json: str, scores_json: str) -> Dict[str, Any]:
            """Get strategic recommendations based on evaluation"""
            try:
                from src.models import ProjectIdea, ScoringResult
                ideas_data = json.loads(ideas_json)
                scores_data = json.loads(scores_json)
                
                ideas = [ProjectIdea(**idea) for idea in ideas_data]
                scores = [ScoringResult(**score) for score in scores_data]
                
                engine = get_recommendation_engine()
                recommendations = engine.generate_recommendations(domain, ideas, scores)
                return {
                    "status": "success",
                    "data": {"recommendations": recommendations}
                }
            except Exception as e:
                logger.error(f"Recommendation error: {e}")
                return {"status": "error", "error": str(e)}

# Create singleton instance
mcp_server = None

def get_mcp_server():
    global mcp_server
    if mcp_server is None:
        mcp_server = IdeaGeneratorMCPServer()
    return mcp_server
