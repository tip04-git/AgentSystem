import random

class RankingAgent:
    def rank(self, hypothesis):
        """Assign a research-based score to the hypothesis."""
        credible_sources = ["ieee", "arxiv", "researchgate", "mit", "nature"]
        
        score = random.randint(5, 10)  # Base score
        
        # Boost score if hypothesis contains trusted sources
        for source in credible_sources:
            if source in hypothesis.lower():
                score += 2
                break  # Only boost once per trusted source
        
        return {"hypothesis": hypothesis, "score": min(score, 10)}
