"""
Main orchestrator - Coordinates all components
"""
from typing import Dict, Any
import logging

from src.domain_analyzer import get_domain_analyzer
from src.idea_generator import get_idea_generator
from src.complexity_estimator import get_complexity_estimator
from src.tech_stack_recommender import get_tech_stack_recommender
from src.scoring_module import get_scoring_module
from src.recommendation_engine import get_recommendation_engine
from src.vector_search import get_vector_search
from src.models import DomainInput, ProjectEvaluation

logger = logging.getLogger(__name__)

class ProjectEvaluationOrchestrator:
    """Orchestrates the full project evaluation pipeline"""
    
    def __init__(self):
        self.domain_analyzer = get_domain_analyzer()
        self.idea_generator = get_idea_generator()
        self.complexity_estimator = get_complexity_estimator()
        self.tech_recommender = get_tech_stack_recommender()
        self.scorer = get_scoring_module()
        self.recommender = get_recommendation_engine()
        self.vector_search = get_vector_search()
    
    def evaluate(self, domain: str, context: str = None, num_ideas: int = 5) -> ProjectEvaluation:
        """Execute full evaluation pipeline"""
        try:
            logger.info(f"Starting evaluation for domain: {domain}")
            
            # Step 1: Analyze domain
            logger.info("Step 1: Analyzing domain...")
            domain_analysis = self.domain_analyzer.analyze(domain, context)
            analysis_text = domain_analysis["analysis"]
            
            # Step 2: Generate ideas
            logger.info("Step 2: Generating ideas...")
            ideas = self.idea_generator.generate(domain, analysis_text, num_ideas)
            
            # Step 3: Estimate complexity
            logger.info("Step 3: Estimating complexity...")
            complexity_analyses = self.complexity_estimator.estimate(ideas)
            
            # Step 4: Recommend tech stacks
            logger.info("Step 4: Recommending tech stacks...")
            tech_stacks = self.tech_recommender.recommend(ideas)
            
            # Step 5: Score ideas
            logger.info("Step 5: Scoring ideas...")
            scores = self.scorer.score(ideas, domain)
            
            # Step 6: Generate recommendations
            logger.info("Step 6: Generating recommendations...")
            recommendations = self.recommender.generate_recommendations(domain, ideas, scores)
            
            # Step 7: Index ideas for future retrieval
            logger.info("Step 7: Indexing ideas for RAG...")
            self._index_ideas(domain, ideas)
            
            evaluation = ProjectEvaluation(
                input_domain=domain,
                ideas=ideas,
                tech_stacks=tech_stacks,
                complexity_analysis=complexity_analyses,
                scoring=scores,
                recommendations=recommendations
            )
            
            logger.info("Evaluation complete!")
            return evaluation
            
        except Exception as e:
            logger.error(f"Evaluation failed: {e}", exc_info=True)
            raise
    
    def _index_ideas(self, domain: str, ideas):
        """Index generated ideas in vector store for RAG"""
        try:
            for i, idea in enumerate(ideas):
                doc_id = f"{domain}_idea_{i}"
                text = f"{idea.title}: {idea.description}. Use case: {idea.use_case}"
                metadata = {
                    "domain": domain,
                    "title": idea.title,
                    "description": idea.description
                }
                self.vector_search.index_document(doc_id, text, metadata)
        except Exception as e:
            logger.warning(f"Failed to index ideas: {e}")

# Singleton instance
_orchestrator = None

def get_orchestrator():
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = ProjectEvaluationOrchestrator()
    return _orchestrator
