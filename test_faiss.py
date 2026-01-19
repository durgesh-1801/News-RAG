import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


DATA_FILE = "backend/data/news.jsonl"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def load_documents():
    docs = []
    with open(DATA_FILE, "r") as f:
        for line in f:
            if line.strip():
                docs.append(json.loads(line)["text"])
    return docs


def main():
    docs = load_documents()
    print(f"[FAISS] Loaded {len(docs)} documents")

    if len(docs) == 0:
        print("❌ No documents found. Run news_writer first.")
        return

    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(docs, convert_to_numpy=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    print(f"[FAISS] Indexed {index.ntotal} documents")

    # 🔍 TEST QUERY
    query = input("\nEnter query: ")
    q_emb = model.encode([query], convert_to_numpy=True)

    D, I = index.search(q_emb, k=3)

    print("\nTop results:")
    for idx in I[0]:
        print("-", docs[idx][:120])


if __name__ == "__main__":
    main()
