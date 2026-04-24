"""
Complexity Estimator - Estimates complexity and development effort
"""
from typing import List, Dict, Any
import openai
import json
from src.config import OPENAI_API_KEY
from src.models import ComplexityAnalysis, ProjectIdea

class ComplexityEstimator:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = "gpt-4"
    
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

Return only valid JSON."""
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_tokens=500
            )
            
            try:
                data = json.loads(response['choices'][0]['message']['content'])
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
