from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3"
)

response = llm.invoke(
    "Explain AI Agent in one paragraph."
)

print(response.content)