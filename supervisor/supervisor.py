from agents.generation import GenerationAgent
from agents.reflection import ReflectionAgent
from agents.ranking import RankingAgent
from agents.evolution import EvolutionAgent
from agents.proximity import ProximityAgent
from agents.metareview import MetaReviewAgent
from storage.memory import Memory

class Supervisor:
    def __init__(self):
        self.memory = Memory()
        self.generation = GenerationAgent()
        self.reflection = ReflectionAgent()
        self.ranking = RankingAgent()
        self.evolution = EvolutionAgent()
        self.proximity = ProximityAgent()
        self.metareview = MetaReviewAgent()

    def process(self, query):
        """Run agents in sequence for a given query."""
        print(f"Processing Query: {query}")

        # Generate idea dynamically from web
        idea = self.generation.generate(query)
        print(f"Generation: {idea}")

        # Reflect on idea
        reflection = self.reflection.reflect(idea)
        print(f"Reflection: {reflection}")

        # Rank the idea based on credibility
        ranked_result = self.ranking.rank(idea)
        print(f"Ranking: {ranked_result['score']}/10")

        # Store initial result
        self.memory.store(query, f"{idea} ({ranked_result['score']}/10)")

        # Evolve the idea
        refined_idea = self.evolution.evolve(idea)
        print(f"Evolution: {refined_idea}")

        # Check proximity (past knowledge)
        past_result = self.proximity.recall(query, self.memory)
        print(f"Proximity: {past_result}")

        # Meta-review feedback
        feedback = self.metareview.review("Process ran smoothly")
        print(f"Meta-review: {feedback}")

        # Store final result
        self.memory.store(query, f"{refined_idea} ({ranked_result['score'] + 1}/10)")

# Test
if __name__ == "__main__":
    supervisor = Supervisor()
    supervisor.process("Quantum Learning")
