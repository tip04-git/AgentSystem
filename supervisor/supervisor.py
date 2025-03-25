import json
import os
from agents.generation import GenerationAgent
from agents.ranking import RankingAgent

class Supervisor:
    def __init__(self):
        self.generation = GenerationAgent()
        self.ranking = RankingAgent()
        self.memory_file = "memory.json"
        self.memory = self.load_memory()  # ✅ Load past data on startup

    def load_memory(self):
        """Load stored research data from file."""
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as file:
                return json.load(file)
        return {}  # Return empty if no file exists

    def save_memory(self):
        """Save research data to file."""
        with open(self.memory_file, "w") as file:
            json.dump(self.memory, file, indent=4)

    def process(self, query):
        """Process user query to generate insights and rank research papers."""
        print(f"\n🔍 Processing Research Topic: {query}")

        # ✅ Check if query exists in memory
        if query in self.memory:
            print("\n🔄 Using previously stored research results...")
            stored_results = self.memory[query]

        else:
            # ✅ Fetch domain summary + latest research
            results = self.generation.generate(query)

            # ✅ Rank research papers
            ranked_papers = self.ranking.rank(query, results["recent_papers"])

            # ✅ Store in memory and save to file
            stored_results = {
                "summary": results["summary"],
                "ranked_papers": ranked_papers
            }
            self.memory[query] = stored_results
            self.save_memory()  # ✅ Save new data to file

        # ✅ Display results
        print("\n📖 **Domain Summary:**")
        print(stored_results["summary"])

        print("\n📑 **Recent Research Papers:**")
        for paper in stored_results["ranked_papers"]:
            year_display = paper["year"] if paper["year"] != "Unknown" else "Year Not Available"
            print(f"\n🔹 **Title:** {paper['title']}")
            print(f"   📅 Year: {year_display}")
            print(f"   🔗 URL: {paper['url']}")
            print(f"   📊 Citations: {paper['citations']}")
            print(f"   📖 References: {paper['references']}")
            print(f"   ⭐ Relevance Score: {paper['score']}/10")

# Test
if __name__ == "__main__":
    supervisor = Supervisor()
    query = input("\nEnter research topic: ")
    supervisor.process(query)
