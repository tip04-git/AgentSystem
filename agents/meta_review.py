import time

class MetaReviewAgent:
    def __init__(self):
        self.start_time = None  # ✅ Store start time dynamically

    def start_timer(self):
        """Start measuring query execution time."""
        self.start_time = time.time()

    def review_performance(self):
        """Check system efficiency and suggest improvements."""
        if self.start_time is None:
            return "⚠️ Timer not started properly."

        elapsed_time = time.time() - self.start_time  # ✅ Correct way to measure query time

        if elapsed_time > 5:  # ✅ If query takes >5s, suggest optimization
            return f"⚡ Query took {elapsed_time:.2f}s. Consider optimizing web requests."
        return f"✅ Query completed in {elapsed_time:.2f}s. Performance is good."
