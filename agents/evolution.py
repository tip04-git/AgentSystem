import random
import re

class EvolutionAgent:
    def __init__(self):
        # ✅ Hardcoded keywords for specific topics
        self.topic_keywords = {
            "AGI": ["Advanced", "Autonomous", "Human-like", "Self-improving", "Scalable"],
            "Quantum Learning": ["Quantum-enhanced", "Entanglement-based", "Superposition-driven", "Quantum-optimized"],
            "Machine Learning": ["Neural-based", "Data-driven", "Deep-learning", "Algorithmic", "Adaptive"],
            "Sustainable Software Design": ["Energy-efficient", "Eco-friendly", "Green-computing", "Sustainable", "Carbon-aware"],
            "Common Sense Reasoning in Agentic AI": ["Context-aware", "Cognitive", "Logical", "Adaptive", "Human-like"]
        }

    def evolve(self, hypothesis, ranked_papers):
        """Refine hypothesis dynamically using topic-based keywords."""
        
        # ✅ Identify topic from hypothesis
        topic = None
        for key in self.topic_keywords:
            if key.lower() in hypothesis.lower():
                topic = key
                break

        # ✅ If topic found, pick a keyword from that category
        if topic:
            selected_word = random.choice(self.topic_keywords[topic])
            return f"{selected_word} {hypothesis}"  # Ensures a logical sentence

        # ✅ If no topic detected, fallback to picking meaningful words from research papers
        valid_words = []
        for paper in ranked_papers:
            words = re.findall(r'\b[A-Za-z]{4,}\b', paper["title"])  # Extract words (min 4 letters)
            for word in words:
                if word.lower() not in hypothesis.lower():
                    valid_words.append(word)

        if valid_words:
            selected_word = random.choice(valid_words)
            return f"{selected_word} in {hypothesis}"

        return hypothesis + " (Refined)"
