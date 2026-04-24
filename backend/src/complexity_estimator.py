"""
Complexity Estimator - Estimates complexity and development effort
"""
from typing import List, Dict, Any
import google.generativeai as genai
import json
import re
from src.config import GOOGLE_API_KEY, GOOGLE_MODEL
from src.models import ComplexityAnalysis, ProjectIdea

class ComplexityEstimator:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(GOOGLE_MODEL)
    
    def estimate(self, ideas: List[ProjectIdea]) -> List[ComplexityAnalysis]:
        """Estimate complexity for each idea"""
        estimations = []
        
        for idea in ideas:
            prompt = f"""Estimate the complexity and development effort for this project idea:

Title: {idea.title}
Description: {idea.description}
Use Case: {idea.use_case}

Provide a JSON response with:
1. overall_score (0-10, where 10 is most complex)
2. development_time (e.g., "2-3 weeks", "1-2 months")
3. difficulty_level (Beginner, Intermediate, or Advanced)
4. key_challenges (list of 3-5 main challenges)

Format:
{{
  "overall_score": 7.5,
  "development_time": "2 months",
  "difficulty_level": "Advanced",
  "key_challenges": ["...", "..."]
}}

Return only valid JSON without markdown formatting."""
            
            response = self.model.generate_content(prompt)
            text_response = response.text
            
            # Clean up possible markdown wrappers
            text_response = re.sub(r'^```json\s*', '', text_response)
            text_response = re.sub(r'^```\s*', '', text_response)
            text_response = re.sub(r'\s*```$', '', text_response)
            text_response = text_response.strip()
            
            try:
                data = json.loads(text_response)
                estimations.append(ComplexityAnalysis(**data))
            except (json.JSONDecodeError, ValueError):
                estimations.append(ComplexityAnalysis(
                    overall_score=5.0,
                    development_time="Unknown",
                    difficulty_level="Intermediate",
                    key_challenges=["Need more analysis"]
                ))
        
        return estimations

# Singleton instance
_estimator = None

def get_complexity_estimator():
    global _estimator
    if _estimator is None:
        _estimator = ComplexityEstimator()
    return _estimator
