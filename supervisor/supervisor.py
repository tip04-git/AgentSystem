from agents.generation import GenerationAgent
from agents.ranking import RankingAgent

class Supervisor:
    def __init__(self):
        self.generation = GenerationAgent()
        self.ranking = RankingAgent()

    def process(self, query):
        """Process user query to generate insights and rank research papers."""
        print(f"\n🔍 Processing Research Topic: {query}")

        # Get general summary + latest research
        results = self.generation.generate(query)

        # Rank research papers
        ranked_papers = self.ranking.rank(query, results["recent_papers"])

        # Display results
        print("\n📖 **Domain Summary:**")
        print(results["summary"])

        print("\n📑 **Recent Research Papers:**")
        for paper, score in ranked_papers:
            print(f"🔹 {paper} | 📊 Relevance Score: {score}/10")  # 🔹 Score now included!

# Test
if __name__ == "__main__":
    supervisor = Supervisor()
    query = input("\nEnter research topic: ")
    supervisor.process(query)
