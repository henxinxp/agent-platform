from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3",
    temperature=0
)

def ask(question:str):

    response = llm.invoke(
        question
    )

    return response.content