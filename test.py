from supervisor.supervisor import Supervisor


# Initialize the Supervisor Agent
supervisor = Supervisor()

# List of two research topics to test
topics = [
    "Quantum Learning",
    "Explainable AI"
]


# Loop through topics and generate research insights
for topic in topics:
    print("\n====================================")
    supervisor.process(topic)
    print("====================================\n")
