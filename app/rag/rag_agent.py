from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from qdrant_client import QdrantClient

llm = ChatOllama(model="qwen3")

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

def ask_rag(question: str):

    client = QdrantClient(
        path="./qdrant_db"
    )

    try:

        query_vector = embeddings.embed_query(
            question
        )

        results = client.query_points(
            collection_name="company_docs",
            query=query_vector,
            limit=1
        )

        context = results.points[0].payload["text"]

        prompt = f"""
Answer the user's question using ONLY the context below.

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        return response.content

    finally:
        client.close()