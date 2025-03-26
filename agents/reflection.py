class ReflectionAgent:
    def reflect(self, query, hypothesis, ranked_papers):
        """Analyze the hypothesis and suggest improvements."""
        if not ranked_papers:
            return f"⚠️ No relevant research found for '{hypothesis}'. Consider broadening the search."

        top_paper = ranked_papers[0]["title"].lower()

        # ✅ If top paper strongly matches query, hypothesis is strong
        if query.lower() in top_paper:
            return f"✅ Hypothesis '{hypothesis}' is well-supported by research."

        # ✅ If relevance score is high, but title doesn't match, suggest a slight refinement
        avg_score = sum(paper["score"] for paper in ranked_papers) / len(ranked_papers)
        if avg_score >= 8:
            return f"🟡 Hypothesis '{hypothesis}' is relevant but could be more precise."

        # ✅ Otherwise, suggest refinement
        return f"⚠️ Hypothesis '{hypothesis}' needs refinement."
