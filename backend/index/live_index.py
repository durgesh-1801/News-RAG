from pathway.xpacks.llm.vector_store import VectorStoreServer


def build_live_index(doc_table):
    return VectorStoreServer(
        docs=doc_table,
        text_column="text",
        metadata_columns=["timestamp"],
        embedding_model="sentence-transformers/all-MiniLM-L6-v2",
    )
