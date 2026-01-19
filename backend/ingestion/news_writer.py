import time
import json
import requests
from backend.config import settings

NEWS_URL = "https://newsapi.org/v2/top-headlines"


def run():
    # Track already-seen URLs (restart-safe)
    seen = set()

    settings.setup_directories()

    # Load existing articles to avoid duplicates after restart
    if settings.news_file.exists():
        with open(settings.news_file, "r") as f:
            for line in f:
                try:
                    seen.add(json.loads(line)["id"])
                except Exception:
                    pass

    print(f"[writer] Loaded {len(seen)} existing articles")

    while True:
        resp = requests.get(
            NEWS_URL,
            params={
                "apiKey": settings.newsapi_key,
                "language": "en",
                "pageSize": 20,   # you can increase to 50 if needed
            },
            timeout=10,
        )
        resp.raise_for_status()

        articles = resp.json().get("articles", [])
        inserted = 0

        with open(settings.news_file, "a") as f:
            for a in articles:
                url = a.get("url")
                if not url or url in seen:
                    continue

                seen.add(url)

                record = {
                    "id": url,
                    "title": a.get("title", ""),
                    "content": a.get("description", ""),
                    "published_at": a.get("publishedAt", ""),
                    "text": f"{a.get('title','')} {a.get('description','')}",
                }

                f.write(json.dumps(record) + "\n")
                inserted += 1

        print(f"[writer] appended {inserted} new articles")
        time.sleep(settings.poll_interval)


if __name__ == "__main__":
    run()
