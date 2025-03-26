import json
import os
import time
from agents.generation import GenerationAgent
from agents.ranking import RankingAgent
from agents.reflection import ReflectionAgent
from agents.evolution import EvolutionAgent
from agents.proximity import ProximityAgent
from agents.meta_review import MetaReviewAgent

class Supervisor:
    def __init__(self):
        self.generation = GenerationAgent()
        self.ranking = RankingAgent()
        self.reflection = ReflectionAgent()
        self.evolution = EvolutionAgent()
        self.proximity = ProximityAgent()
        self.meta_review = MetaReviewAgent()
        #self.memory={}
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
        """Process user query using multiple agents and improve hypothesis over multiple cycles."""
        print("\n" + "="*60)
        print(f"🔍 **Processing Research Topic:** {query}")
        print("="*60)

         # ✅ Step 1: Start Timer (before processing begins)
        self.meta_review.start_timer()

        # ✅ Step 2: Check past research using Proximity Agent
        proximity_feedback = self.proximity.check_past_results(query, self.memory)
        print(f"\n📌 **Proximity Check:** {proximity_feedback}")

         # ✅ Step 3: Check if query exists in memory
        if query in self.memory:
            stored_results = self.memory[query]
    
            # ✅ If hypothesis contains broken structure, reset it
            if " in AI-driven Landscape" in stored_results["hypothesis"]:
                print("⚠️ **Bad hypothesis detected. Resetting...**")
                stored_results["hypothesis"] = query  # Reset to original query

            print("🔄 **Using previously stored research results...**")

            # ✅ Force Reflection & Evolution
            ranked_papers = stored_results["ranked_papers"]
            hypothesis = stored_results["hypothesis"]
            reflection_feedback = self.reflection.reflect(query, hypothesis, ranked_papers)
            print(f"\n🧐 **Reflection Analysis:** {reflection_feedback}")

            if "needs refinement" in reflection_feedback:
                hypothesis = self.evolution.evolve(hypothesis, ranked_papers)
                print(f"🔄 **Evolved Hypothesis:** {hypothesis}")

            # ✅ Update stored hypothesis
            stored_results["hypothesis"] = hypothesis
            self.memory[query] = stored_results
            self.save_memory()
        else:
            # ✅ Step 4: Generate initial research & ranking
            results = self.generation.generate(query)
            ranked_papers = self.ranking.rank(query, results["recent_papers"])

            # ✅ Step 5: Reflection Agent checks relevance
            hypothesis = query  # Use query as initial hypothesis
            reflection_feedback = self.reflection.reflect(query, hypothesis, ranked_papers)
            print(f"\n🧐 **Reflection Analysis:** {reflection_feedback}")

            # ✅ Step 6: Evolution Agent refines hypothesis
            if "needs refinement" in reflection_feedback:
                hypothesis = self.evolution.evolve(hypothesis)
                print(f"🔄 **Evolved Hypothesis:** {hypothesis}")

            # ✅ Step 7: Store updated data in memory
            stored_results = {
                "summary": results["summary"],
                "ranked_papers": ranked_papers,
                "hypothesis": hypothesis
            }
            self.memory[query] = stored_results
            self.save_memory()

        # ✅ Step 8: Display results
        print("\n📖 **Domain Summary:**\n" + "-"*50)
        print(f"{stored_results['summary']}\n")

        print("\n📑 **Recent Research Papers:**")
        for paper in stored_results["ranked_papers"]:
            print("\n------------------------------------------")
            print(f"\n 🔹 **Title:** {paper['title']}")
            print(f"   📅 **Year:** {paper['year']}")
            print(f"   🔗 **URL:** {paper['url']}")
            print(f"   📊 **Citations:** {paper['citations']}")
            print(f"   📖 **References:** {paper['references']}")
            print(f"   ⭐ **Relevance Score:** {paper['score']}/10")
        print("------------------------------------------")

        # ✅ Step 9: Stop Timer & Print Meta-review Report
        total_time = self.meta_review.review_performance()
        print(f"\n📊 **Meta-Review Report:** {total_time}")

        print("\n" + "="*50)

# Test
if __name__ == "__main__":
    supervisor = Supervisor()
    query = input("\nEnter research topic: ")
    supervisor.process(query)
