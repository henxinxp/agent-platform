from langchain_ollama import OllamaEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

client = QdrantClient(
    path="./qdrant_db"
)

collection_name = "company_docs"

try:
    try:
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=768,
                distance=Distance.COSINE
            ),
        )
        print("Collection created")
    except Exception:
        print("Collection already exists")

    with open(
        "data/docs/company.txt",
        "r",
        encoding="utf-8"
    ) as f:
        text = f.read()

    vector = embeddings.embed_query(text)

    client.upsert(
        collection_name=collection_name,
        points=[
            PointStruct(
                id=1,
                vector=vector,
                payload={
                    "text": text
                }
            )
        ]
    )

    print("Document loaded into Qdrant")

finally:
    client.close()