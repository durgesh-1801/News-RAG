import time
import json
import requests
import pathway as pw
from backend.config import settings

NEWS_URL = "https://newsapi.org/v2/top-headlines"


class NewsSchema(pw.Schema):
    id: str
    text: str
    published_at: str


def news_generator():
    seen = set()
    while True:
        resp = requests.get(
            NEWS_URL,
            params={
                "apiKey": settings.newsapi_key,
                "language": "en",
                "pageSize": 5,
            },
            timeout=10,
        )
        resp.raise_for_status()

        for a in resp.json().get("articles", []):
            url = a.get("url")
            if not url or url in seen:
                continue

            seen.add(url)

            yield {
                "id": url,
                "text": f"{a.get('title','')} {a.get('description','')}",
                "published_at": a.get("publishedAt", ""),
            }

        time.sleep(settings.poll_interval)


def run():
    table = pw.io.python.read(
        pw.io.python.ConnectorSubject(news_generator),
        schema=NewsSchema,
        mode="streaming",
    )

    # 🔑 THIS IS THE ANCHOR — without this Pathway exits
    table.select(pw.this.id).debug()


if __name__ == "__main__":
    run()
    pw.run()
