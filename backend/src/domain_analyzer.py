"""
Domain Analyzer - Analyzes input domain/idea for key characteristics
"""
from typing import Dict, List, Any
import openai
from src.config import OPENAI_API_KEY

class DomainAnalyzer:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = "gpt-4"
    
    def analyze(self, domain: str, context: str = None) -> Dict[str, Any]:
        """Analyze domain and extract key characteristics"""
        prompt = f"""Analyze the following domain/idea and provide structured insights:

Domain: {domain}
{"Context: " + context if context else ""}

Provide analysis in the following format:
1. Main problem areas
2. Key stakeholders
3. Current solutions/competitors
4. Market size estimation
5. Technical requirements
6. Industry trends

Be concise but comprehensive."""
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )
        
        return {
            "domain": domain,
            "analysis": response['choices'][0]['message']['content']
        }

# Singleton instance
_analyzer = None

def get_domain_analyzer():
    global _analyzer
    if _analyzer is None:
        _analyzer = DomainAnalyzer()
    return _analyzer
