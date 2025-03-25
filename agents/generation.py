import requests
import re

class GenerationAgent:
    def __init__(self):
        self.google_api_key = "AIzaSyDGyS_4iz_RkuvoAn0r4fDfnX6i-lZ7Qfg"
        self.cx = "90939ac65eade482d"

    def fetch_from_google(self, query):
        """Fetch domain summary and research papers from Google."""
        research_query = f"{query} latest research 2024 OR recent studies site:arxiv.org OR site:researchgate.net OR site:nature.com OR site:sciencedirect.com"
        general_query = f"{query} key concepts OR applications OR overview"

        # URLs for Google Search API
        research_url = f"https://www.googleapis.com/customsearch/v1?q={research_query}&key={self.google_api_key}&cx={self.cx}"
        general_url = f"https://www.googleapis.com/customsearch/v1?q={general_query}&key={self.google_api_key}&cx={self.cx}"

        try:
            # Fetch general domain insights
            general_response = requests.get(general_url).json()
            domain_info = []
            for item in general_response.get("items", [])[:2]:  # Get top 2 sources
                snippet = item["snippet"]

                # Remove unnecessary dates like "Mar 17, 2020"
                snippet = re.sub(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}\b", "", snippet)

                # Remove special characters and ending "..."
                snippet = snippet.replace("\xa0", " ").strip()
                if snippet.endswith("..."):
                    snippet = snippet[:-3]

                domain_info.append(snippet)

            # Combine into a short summary
            short_summary = " ".join(domain_info) if domain_info else "No relevant domain summary found."

            # Fetch research papers
            research_response = requests.get(research_url).json()
            papers = []
            if "items" in research_response:
                for item in research_response["items"][:3]:  # Get top 3 papers
                    title = item["title"]
                    snippet = item.get("snippet", "").replace("\xa0", " ")

                    # Extract year from snippet if available
                    year_match = re.search(r"\b(19|20)\d{2}\b", snippet)
                    year = year_match.group() if year_match else "Year Not Found"

                    papers.append(f"{title} (Published: {year})")

            # If no papers were found, add a placeholder
            if not papers:
                papers.append("No relevant research papers found.")

            return short_summary, papers
        except Exception as e:
            return f"Error fetching data from Google: {e}", ["No research papers available due to an error."]

    def generate(self, query):
        """Generate a structured domain summary and relevant research papers."""
        domain_summary, recent_papers = self.fetch_from_google(query)

        return {
            "summary": domain_summary,
            "recent_papers": recent_papers
        }