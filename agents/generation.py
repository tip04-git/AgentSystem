import requests

class GenerationAgent:
    def __init__(self):
        self.api_key = "AIzaSyCTaSsEkaDseC9kWn2-DI6AVXsP63YOvgc"  # Replace with your actual Google API Key
        self.cx = "90939ac65eade482d"  # Your correct CX Code

    def generate(self, query):
        """Fetch research ideas from Google Custom Search API."""
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={self.api_key}&cx={self.cx}"

        try:
            response = requests.get(url)
            data = response.json()

            if "items" in data and len(data["items"]) > 0:
                return data["items"][0]["title"]  # Extract first search result title
            return "No relevant research found."
        except Exception as e:
            return f"Error fetching data: {e}"
