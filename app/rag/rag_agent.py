from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

from qdrant_client import QdrantClient

from app.memory.chat_memory import (
    add_message,
    get_history
)


from app.memory.memory_store import get_history


llm = ChatOllama(
    model="qwen2.5:0.5b",
    temperature=0
)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


def ask_rag(
    session_id,
    question
):

    client = QdrantClient(
        path="./qdrant_db"
    )

    try:

        history = get_history(
            session_id
        )

        history_text = ""

        for msg in history[-10:]:

            history_text += (
                f"{msg['role']}: "
                f"{msg['content']}\n"
            )

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
Conversation History:

{history_text}

Context:

{context}

Question:

{question}

Answer:
"""

        response = llm.invoke(
            prompt
        )

        return response.content

    finally:

        client.close()