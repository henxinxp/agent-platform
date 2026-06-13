from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:0.5b",
    temperature=0
)

def choose_tool(question: str):

    prompt = f"""
You are a routing engine.

Available tools:

calculator
- math
- arithmetic
- calculations

rag
- company policy
- employee information
- internal knowledge

weather
- weather
- temperature
- forecast
- climate

Question:
{question}

Reply ONLY with one word:

calculator
rag
weather
"""

    result = llm.invoke(prompt)

    tool = result.content.strip().lower()

    print("RAW ROUTER:", tool)

    if "weather" in tool:
        return "weather"

    if "calculator" in tool:
        return "calculator"

    return "rag"