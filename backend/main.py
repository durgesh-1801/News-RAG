import argparse
import pathway as pw

from backend.ingestion.news_stream import pathway_news_table
from backend.pipeline.streaming_pipeline import build_pipeline
from backend.index.live_index import build_live_index
from backend.api.query_service import answer_query


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ask", type=str, required=True)
    args = parser.parse_args()

    news_table = pathway_news_table()
    processed = build_pipeline(news_table)
    vector_server = build_live_index(processed)

    pw.run_async()
    pw.wait_for_seconds(10)

    answer = answer_query(vector_server, args.ask)
    print("\nANSWER:\n")
    print(answer)


if __name__ == "__main__":
    main()
