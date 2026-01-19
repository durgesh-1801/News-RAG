import pathway as pw
from backend.pipeline.rag_pipeline import create_rag_server

if __name__ == "__main__":
    server = create_rag_server(streaming=True)

    server.run_server(
        host="127.0.0.1",
        port=8080,
        with_cache=True,
    )

    pw.run()
