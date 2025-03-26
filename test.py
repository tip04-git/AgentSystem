'''/*from supervisor.supervisor import Supervisor

# ✅ Initialize the Supervisor Agent
supervisor = Supervisor()

# ✅ List of research topics to test
topics = [
    #"Quantum Learning",
    "Explainable AI",
    #"Artificial Intelligence"
]

# ✅ Loop through topics and generate research insights
for topic in topics:
    supervisor.process(topic)  # ✅ Now, it will check memory before fetching new data
    print("====================================\n")'''

from supervisor.supervisor import Supervisor
supervisor=Supervisor()
while True:
    # ✅ Take user input for the research topic
    topic = input("\n🔍 Enter a research topic (or type 'exit' to stop): ").strip()
    if topic.lower() == "exit":
        print("🚀 Research session ended.")
        break  # Exit the loop
    # ✅ Process the user-entered topic
    supervisor.process(topic)
    print("\n====================================\n")

