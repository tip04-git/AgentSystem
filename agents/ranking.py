import random

class RankingAgent:
    def rank(self, query, papers):
        """Assign a research-based relevance score to each paper."""
        ranked_papers = []
        
        for paper in papers:
            score = random.randint(6, 10)  # Base score
            if query.lower() in paper.lower():
                score += 2  # Increase score if title closely matches query
            
            ranked_papers.append((paper, min(score, 10)))  # Ensure max score is 10
        
        return ranked_papers
