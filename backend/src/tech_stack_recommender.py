"""
Tech Stack Recommender - Recommends technology stack for each idea
"""
from typing import List, Dict, Any
import openai
import json
from src.config import OPENAI_API_KEY
from src.models import ProjectIdea, TechStackItem

class TechStackRecommender:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = "gpt-4"
    
    def recommend(self, ideas: List[ProjectIdea]) -> List[List[TechStackItem]]:
        """Recommend tech stack for each idea"""
        all_stacks = []
        
        for idea in ideas:
            prompt = f"""Recommend a modern technology stack for this project:

Title: {idea.title}
Description: {idea.description}
Use Case: {idea.use_case}

Recommend tools in these categories:
- Backend Framework
- Database
- Frontend Framework
- Deployment/Hosting
- AI/ML Libraries (if applicable)

For each, explain why it's suitable.

Format response as JSON array:
[
  {{"category": "Backend Framework", "tool": "FastAPI", "reason": "..."}},
  ...
]

Return only valid JSON."""
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=800
            )
            
            try:
                stack_data = json.loads(response['choices'][0]['message']['content'])
                tech_stack = [TechStackItem(**item) for item in stack_data]
                all_stacks.append(tech_stack)
            except (json.JSONDecodeError, ValueError):
                all_stacks.append([
                    TechStackItem(category="Backend", tool="FastAPI", reason="Modern async framework"),
                    TechStackItem(category="Database", tool="PostgreSQL", reason="Reliable relational DB"),
                    TechStackItem(category="Frontend", tool="React", reason="Component-based UI"),
                ])
        
        return all_stacks

# Singleton instance
_recommender = None

def get_tech_stack_recommender():
    global _recommender
    if _recommender is None:
        _recommender = TechStackRecommender()
    return _recommender
