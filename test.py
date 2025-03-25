from agents.generation import GenerationAgent

gen_agent = GenerationAgent()

topics = [
    "AGI",
    "Quantum Learning",
    "Machine Unlearning",
    "Sustainable Software Design",
    "Common Sense Reasoning in Agentic AI",
    "AI Ethics and Bias",
    "Neuromorphic Computing",
    "Self-Supervised Learning",
    "Explainable AI",
    "Edge AI"
]

for topic in topics:
    result = gen_agent.generate(topic)
    print(f"Topic: {topic} | Generated Hypothesis: {result}")
