"""
Idea Generator - Generates project ideas based on domain analysis
"""
from typing import List, Dict, Any
import openai
import json
from src.config import OPENAI_API_KEY
from src.models import ProjectIdea

class IdeaGenerator:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = "gpt-4"
    
    def generate(self, domain: str, analysis: str, num_ideas: int = 5) -> List[ProjectIdea]:
        """Generate project ideas for the domain"""
        prompt = f"""Based on the following domain analysis, generate {num_ideas} innovative project ideas.

Domain: {domain}

Analysis:
{analysis}

For each idea, provide:
1. A creative project title
2. A detailed description (2-3 sentences)
3. Primary use case
4. Potential impact

Format your response as a JSON array with objects containing: title, description, use_case, potential_impact

Example format:
[
  {{"title": "...", "description": "...", "use_case": "...", "potential_impact": "..."}}
]

Generate exactly {num_ideas} ideas. Return only valid JSON."""
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9,
            max_tokens=2000
        )
        
        try:
            ideas_data = json.loads(response['choices'][0]['message']['content'])
            return [ProjectIdea(**idea) for idea in ideas_data]
        except (json.JSONDecodeError, ValueError) as e:
            # Fallback if JSON parsing fails
            return [
                ProjectIdea(
                    title=f"Project Idea {i+1}",
                    description=response['choices'][0]['message']['content'][:200],
                    use_case="To be detailed",
                    potential_impact="High"
                )
                for i in range(num_ideas)
            ]

# Singleton instance
_generator = None

def get_idea_generator():
    global _generator
    if _generator is None:
        _generator = IdeaGenerator()
    return _generator
