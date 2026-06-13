from langchain_ollama import OllamaEmbeddings
from qdrant_client import QdrantClient

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

client = QdrantClient(
    path="./qdrant_db"
)

query = "How many vacation days do employees have?"

query_vector = embeddings.embed_query(query)

results = client.query_points(
    collection_name="company_docs",
    query=query_vector,
    limit=1
)

print(results.points[0].payload["text"])

client.close()