from app.graph.agent_graph import agent

tests = [

    "25 * 18",

    "How many vacation days do employees have?",

    "What is weather in Toronto?",

    "Who is the Prime Minister of Canada?"
]

for q in tests:

    result = agent.invoke(
        {
            "question": q
        }
    )

    print()
    print("=" * 50)
    print("QUESTION:", q)
    print("ANSWER:")
    print(result["answer"])