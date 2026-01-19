import os
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    # -------------------
    # API Keys
    # -------------------
    newsapi_key: str = os.getenv("NEWS_API_KEY", "")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

    # -------------------
    # Server
    # -------------------
    host: str = os.getenv("HOST", "127.0.0.1")
    port: int = int(os.getenv("PORT", "8080"))

    # -------------------
    # Polling
    # -------------------
    poll_interval: int = int(os.getenv("POLL_INTERVAL", "30"))

    # -------------------
    # Embeddings (THIS WAS MISSING)
    # -------------------
    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    # -------------------
    # Paths
    # -------------------
    base_dir: Path = Path(__file__).resolve().parent

    @property
    def data_dir(self) -> Path:
        return self.base_dir / "data"

    @property
    def news_file(self) -> Path:
        return self.data_dir / "news.jsonl"

    def setup_directories(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)
        if not self.news_file.exists():
            self.news_file.touch()


settings = Settings()
