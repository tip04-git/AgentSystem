class ProximityAgent:
    def check_past_results(self, query, memory):
        """Check if a similar topic has been researched before."""
        for past_query in memory:
            if query.lower() in past_query.lower():
                return f"🔄 Using past research on '{past_query}'."
        
        return "🆕 No past research found for this topic."
