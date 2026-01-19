# Real-Time News Retrieval-Augmented Generation (RAG) System

## 📌 Project Overview

This project implements a **Real-Time News Retrieval-Augmented Generation (RAG) pipeline** that ingests live news articles, converts them into dense vector embeddings, and enables **semantic search** over the latest news using **FAISS**.

Instead of keyword-based search, the system retrieves news articles based on **semantic similarity**, ensuring more relevant and context-aware results.

The project focuses on:
- Real-time data ingestion
- Efficient document storage
- Vector-based semantic retrieval
- Practical, submission-ready architecture

---

## 🧠 Key Features

- 🔄 Live news ingestion using NewsAPI
- 🧹 Deduplication of articles using URL hashing
- 📄 Persistent document storage (JSONL format)
- 🔢 Dense embeddings using SentenceTransformers
- ⚡ Fast similarity search using FAISS
- 💻 CLI-based querying interface

---

## 🏗️ Project Architecture

NewsAPI
↓
Ingestion (news_writer.py)
↓
JSONL Document Store
↓
SentenceTransformer Embeddings
↓
FAISS Vector Index
↓
Semantic Retrieval (Top-K)
↓
CLI Output

---

## 📁 Project Structure

data_quest/
│
├── backend/
│ ├── ingestion/
│ │ └── news_writer.py # Fetches and stores live news
│ │
│ ├── data/
│ │ └── news.jsonl # Stored news articles (JSON Lines)
│ │
│ └── config.py # Environment & path configuration
│
├── test_faiss.py # FAISS indexing + query interface
├── requirements.txt # Python dependencies
├── .env # API keys (not committed)
└── README.md


---

## ⚙️ Prerequisites

- Python **3.10 or 3.11**
- NewsAPI API key  
  (https://newsapi.org/)
- OS: Linux / macOS / Windows (WSL recommended)

---

## 🔐 Environment Setup

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd data_quest
```
Create & activate virtual environment
```bash
python -m venv pathway-env
source pathway-env/bin/activate
```
Install dependencies
```
pip install -r requirements.txt
```
Environment Variables

Create a .env file in the project root:
```
NEWS_API_KEY=your_newsapi_key_here
```
Step 1: Run News Ingestion
This script continuously fetches live news and stores them locally.
```
python backend/ingestion/news_writer.py
```
What this does:


Fetches latest news from NewsAPI


Deduplicates articles


Appends articles to backend/data/news.jsonl


Stop anytime using:
CTRL + C


🔍 Step 2: Run FAISS Semantic Search
Once news is collected, run:
```
python test_faiss.py
```
You will see:
[FAISS] Loaded XX documents
[FAISS] Indexed XX documents
Enter query:

Example Queries
africa vaccine
technology startup
global trade agreement
sports tournament

The system returns Top-K semantically relevant articles.

✅ What Is Completed
✔ Real-time ingestion
✔ Persistent storage
✔ Dense embeddings
✔ FAISS indexing
✔ Semantic search
✔ CLI-based querying

❌ What Is Intentionally Excluded


Frontend UI (CLI used instead)


LLM answer generation (retrieval-focused RAG)


Metadata filtering (future enhancement)



🚀 Future Enhancements


LLM-based answer generation


Web UI (Streamlit / FastAPI)


Metadata filters (date, category)


Deployment as an API service



📊 Sample Output
Query: africa vaccine

Top results:
- RFK-backed infant vaccine study in Africa – Washington Post
- Related international health policy news
- Additional contextually relevant articles


🧪 Evaluation Notes


Uses industry-grade FAISS indexing


Designed for real-time updates


Scales efficiently with growing data


Submission-aligned, reproducible pipeline



Made for IIT KGP DATA quest 

📄 License
This project is for academic and educational use.

---

