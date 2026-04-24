from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class DomainInput(BaseModel):
    """User input containing domain/idea"""
    domain: str
    context: Optional[str] = None

class ProjectIdea(BaseModel):
    """Generated project idea"""
    title: str
    description: str
    use_case: str
    potential_impact: str

class TechStackItem(BaseModel):
    """Technology in the stack"""
    category: str
    tool: str
    reason: str

class ComplexityAnalysis(BaseModel):
    """Complexity estimation"""
    overall_score: float  # 0-10
    development_time: str  # e.g., "2-3 weeks"
    difficulty_level: str  # Beginner, Intermediate, Advanced
    key_challenges: List[str]

class ScoringResult(BaseModel):
    """Final scoring and evaluation"""
    feasibility_score: float  # 0-100
    innovation_score: float  # 0-100
    market_potential_score: float  # 0-100
    overall_score: float  # 0-100
    breakdown: Dict[str, Any]

class ProjectEvaluation(BaseModel):
    """Complete project evaluation"""
    input_domain: str
    ideas: List[ProjectIdea]
    tech_stacks: List[List[TechStackItem]]
    complexity_analysis: List[ComplexityAnalysis]
    scoring: List[ScoringResult]
    recommendations: List[str]

class MCPToolResult(BaseModel):
    """Result from MCP tool execution"""
    tool_name: str
    status: str
    data: Dict[str, Any]
    error: Optional[str] = None
