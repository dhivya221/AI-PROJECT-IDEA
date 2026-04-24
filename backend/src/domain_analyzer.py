"""
Domain Analyzer - Analyzes input domain/idea for key characteristics
"""
from typing import Dict, List, Any
import google.generativeai as genai
from src.config import GOOGLE_API_KEY, GOOGLE_MODEL

class DomainAnalyzer:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(GOOGLE_MODEL)
    
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
        
        response = self.model.generate_content(prompt)
        
        return {
            "domain": domain,
            "analysis": response.text
        }

# Singleton instance
_analyzer = None

def get_domain_analyzer():
    global _analyzer
    if _analyzer is None:
        _analyzer = DomainAnalyzer()
    return _analyzer
