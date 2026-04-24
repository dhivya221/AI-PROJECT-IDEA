"""
Tech Stack Recommender - Recommends technology stack for each idea
"""
from typing import List, Dict, Any
import google.generativeai as genai
import json
import re
from src.config import GOOGLE_API_KEY, GOOGLE_MODEL
from src.models import ProjectIdea, TechStackItem

class TechStackRecommender:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(GOOGLE_MODEL)
    
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

Return only valid JSON without markdown formatting."""
            
            response = self.model.generate_content(prompt)
            text_response = response.text
            
            # Clean up possible markdown wrappers
            text_response = re.sub(r'^```json\s*', '', text_response)
            text_response = re.sub(r'^```\s*', '', text_response)
            text_response = re.sub(r'\s*```$', '', text_response)
            text_response = text_response.strip()
            
            try:
                stack_data = json.loads(text_response)
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
