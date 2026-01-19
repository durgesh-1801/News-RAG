import pathway as pw
from pathway.xpacks.llm.vector_store import VectorStoreServer
from backend.config import settings
from langchain_community.embeddings import HuggingFaceEmbeddings


class RawNewsSchema(pw.Schema):
    doc_id: str
    text: str
    published_at: str


def create_document_stream() -> pw.Table:
    raw = pw.io.jsonlines.read(
        path=str(settings.news_file),
        schema=RawNewsSchema,
        mode="streaming",
    )

    # 🔑 ADAPT to Pathway DocumentStore contract
    docs = raw.select(
        data=pw.this.text,          # REQUIRED column name
        _metadata=pw.apply(
            lambda doc_id, published_at: {
                "doc_id": doc_id,
                "published_at": published_at,
            },
            pw.this.doc_id,
            pw.this.published_at,
        ),
    )

    return docs


def create_rag_server(streaming: bool = True) -> VectorStoreServer:
    docs = create_document_stream()

    embedder = HuggingFaceEmbeddings(
        model_name=settings.embedding_model
    )

    server = VectorStoreServer.from_langchain_components(
        docs,
        embedder=embedder,
    )

    return server
