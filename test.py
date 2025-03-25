from supervisor.supervisor import Supervisor

# ✅ Initialize the Supervisor Agent
supervisor = Supervisor()

# ✅ List of research topics to test
topics = [
    "Quantum Learning",
    #"Explainable AI"
]

# ✅ Loop through topics and generate research insights
for topic in topics:
    print("\n====================================")
    supervisor.process(topic)  # ✅ Now, it will check memory before fetching new data
    print("====================================\n")
