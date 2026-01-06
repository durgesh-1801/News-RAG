import google.generativeai as genai
from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def answer_query(vector_server, question: str) -> str:
    docs = vector_server.similarity_search(question, k=5)
    context = "\n".join(d["text"] for d in docs)

    prompt = f"""
You are a real-time news analyst.
Answer using ONLY the latest news context.

Context:
{context}

Question:
{question}
"""

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
