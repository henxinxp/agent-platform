from app.graph.agent_graph import agent

result = agent.invoke(
    {
        "question":"What is weather in Toronto?"
    }
)

print(result)

result = agent.invoke(
    {
        "question":"25*18"
    }
)

print(result)

result = agent.invoke(
    {
        "question":"How many vacation days?"
    }
)

print(result)