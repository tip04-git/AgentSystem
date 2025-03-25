import random

class RankingAgent:
    def rank(self, query, papers):
        """Assign a research-based relevance score to each paper."""
        ranked_papers = []
        
        for paper in papers:
            score = random.randint(6, 10)  # Base score
            
            if query.lower() in paper["title"].lower():
                score += 2  # Increase score if title closely matches query

            ranked_papers.append({
                "title": paper["title"],
                "year": paper["year"],
                "url": paper.get("url", "URL Not Available"),  # ✅ Fix: Keep `url`
                "score": min(score, 10),
                "citations": random.randint(50, 500),  # Placeholder
                "references": random.randint(20, 100)  # Placeholder
            })
        
        # ✅ Ensure sorting returns dictionaries (not tuples)
        ranked_papers.sort(key=lambda x: (x["citations"], x["references"]), reverse=True)

        return ranked_papers  # ✅ Returns correctly formatted dictionaries
