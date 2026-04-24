"""
Recommendation Engine - Generates recommendations based on analysis
"""
from typing import List, Dict, Any
import google.generativeai as genai
from src.config import GOOGLE_API_KEY, GOOGLE_MODEL
from src.models import ProjectIdea, ScoringResult

class RecommendationEngine:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(GOOGLE_MODEL)
    
    def generate_recommendations(
        self,
        domain: str,
        ideas: List[ProjectIdea],
        scores: List[ScoringResult]
    ) -> List[str]:
        """Generate actionable recommendations based on evaluation"""
        
        # Create summary of top ideas
        ideas_summary = "\n".join([
            f"- {idea.title} (Score: {score.overall_score}): {idea.description}"
            for idea, score in zip(ideas, scores)
        ])
        
        prompt = f"""Based on the domain analysis and project evaluations, provide 5-7 strategic recommendations:

Domain: {domain}

Top Ideas:
{ideas_summary}

Provide recommendations for:
1. Which idea to prioritize and why
2. Key milestones and timeline
3. Required team composition
4. Potential partnerships or resources needed
5. Risk mitigation strategies
6. Path to MVP and subsequent phases

Format as a numbered list of actionable recommendations."""
        
        response = self.model.generate_content(prompt)
        
        content = response.text
        # Parse numbered list
        recommendations = [
            line.strip() for line in content.split('\n')
            if line.strip() and any(char.isdigit() for char in line[:3])
        ]
        
        return recommendations if recommendations else [content]

# Singleton instance
_engine = None

def get_recommendation_engine():
    global _engine
    if _engine is None:
        _engine = RecommendationEngine()
    return _engine
