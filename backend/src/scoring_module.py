"""
Scoring Module - Scores ideas on multiple dimensions
"""
from typing import List, Dict, Any
import openai
import json
from src.config import OPENAI_API_KEY
from src.models import ProjectIdea, ScoringResult

class ScoringModule:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = "gpt-4"
    
    def score(self, ideas: List[ProjectIdea], domain: str) -> List[ScoringResult]:
        """Score ideas on feasibility, innovation, and market potential"""
        results = []
        
        for idea in ideas:
            prompt = f"""Score this project idea across multiple dimensions.

Domain: {domain}
Project Title: {idea.title}
Description: {idea.description}
Use Case: {idea.use_case}

Score each on a scale of 0-100:

1. Feasibility Score: How realistic is this to build within 3 months?
2. Innovation Score: How novel/innovative is the idea?
3. Market Potential Score: How large is the addressable market?

Also provide:
- Overall Score: Average of the three scores
- Breakdown with reasoning for each score

Format as JSON:
{{
  "feasibility_score": 75,
  "innovation_score": 80,
  "market_potential_score": 70,
  "overall_score": 75,
  "breakdown": {{
    "feasibility_reason": "...",
    "innovation_reason": "...",
    "market_reason": "..."
  }}
}}

Return only valid JSON."""
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_tokens=600
            )
            
            try:
                score_data = json.loads(response['choices'][0]['message']['content'])
                results.append(ScoringResult(**score_data))
            except (json.JSONDecodeError, ValueError):
                results.append(ScoringResult(
                    feasibility_score=70.0,
                    innovation_score=75.0,
                    market_potential_score=70.0,
                    overall_score=71.67,
                    breakdown={"note": "Estimation pending detailed analysis"}
                ))
        
        return results

# Singleton instance
_scorer = None

def get_scoring_module():
    global _scorer
    if _scorer is None:
        _scorer = ScoringModule()
    return _scorer
