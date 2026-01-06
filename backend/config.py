import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWS_LANGUAGE = "en"
POLL_INTERVAL_SECONDS = 30
