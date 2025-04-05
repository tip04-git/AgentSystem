import requests
import re
import time
from dotenv import load_dotenv
import os

load_dotenv()
class GenerationAgent:
    def __init__(self):
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.cx =os.getenv("GOOGLE_CX")

    def fetch_from_google(self, query):
        """Fetch research papers from Google Search, ensuring quality results."""
        
        # To create Artificial Delay(To trigger Consider optimizing web requests command.) 
        #print("\n⏳ Simulating a slow query...")
        #time.sleep(6)  # ✅ Artificial delay to trigger Meta-review warning
        #print("\n⏳ Fetching real-time data...")  

        research_query = f"{query} latest research 2024 OR recent studies site:arxiv.org OR site:researchgate.net OR site:nature.com OR site:sciencedirect.com"
        research_url = f"https://www.googleapis.com/customsearch/v1?q={research_query}&key={self.google_api_key}&cx={self.cx}"

        try:
            response = requests.get(research_url).json()
            papers = []
            
            for item in response.get("items", [])[:3]:  # Get top 3 papers
                title = item.get("title", "").strip()  # Ensure title is fully displayed
                snippet = item.get("snippet", "").replace("\xa0", " ")
                link = item.get("link", "")

                # Extract publication year from snippet or URL
                year_match = re.search(r"\b(19|20)\d{2}\b", snippet) or re.search(r"\b(19|20)\d{2}\b", link)
                year = year_match.group() if year_match else "Unknown"

                papers.append({
                    "title": title,
                    "url": link,
                    "year": year,
                    # Google doesn't provide this, so keeping as "Unknown"
                })


            return papers
        except Exception as e:
            print(f"Error fetching from Google: {e}")
            return []
    def fetch_domain_summary(self, query):
        """Fetch an in-depth domain summary from Google."""
        general_query = f"{query} overview OR introduction OR key concepts OR applications"
        general_url = f"https://www.googleapis.com/customsearch/v1?q={general_query}&key={self.google_api_key}&cx={self.cx}"

        try:
            general_response = requests.get(general_url).json()
            domain_info = []
        
            for item in general_response.get("items", [])[:3]:  # Get top 3 sources
                snippet = item["snippet"].replace("\xa0", " ").strip()

                # ✅ Remove unnecessary dates like "Dec 18, 2024"
                snippet = re.sub(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}\b", "", snippet)

                # ✅ Remove unnecessary "..." at the end
                snippet = snippet.replace("...", " ")

                # ✅ Remove redundant words like "AI has attained great accuracy not just..."
                snippet = re.sub(r"\b(AI has attained great accuracy.*?not just)\b", "", snippet, flags=re.IGNORECASE)

                domain_info.append(snippet)

            # ✅ Ensure proper sentence structure
            full_summary = " ".join(domain_info)
        
            # ✅ Capitalize first letter and ensure proper ending punctuation
            if full_summary:
                full_summary = full_summary[0].upper() + full_summary[1:]  # Capitalize first letter
                if not full_summary.endswith("."):
                    full_summary += "."

        except Exception as e:
            full_summary = f"Error fetching domain summary: {e}"

        return full_summary

    def generate(self, query):
        """Generate a structured domain summary and relevant research papers."""
        print(f"Fetching research papers for: {query}")

    # Fetch detailed domain summary
        full_summary = self.fetch_domain_summary(query)

    # Fetch research papers
        google_papers = self.fetch_from_google(query)

        return {
            "summary": full_summary,  # ✅ Fix: More relevant content
            "recent_papers": google_papers
        }

