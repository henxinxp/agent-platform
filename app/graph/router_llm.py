def choose_tool(question: str):

    q = question.lower()

    # calculator
    if any(
        op in q
        for op in [
            "+",
            "-",
            "*",
            "/"
        ]
    ):
        return "calculator"

    # weather
    if any(
        word in q
        for word in [
            "weather",
            "temperature",
            "forecast"
        ]
    ):
        return "weather"

    # web search
    if any(
        word in q
        for word in [
            "today",
            "latest",
            "news",
            "current",
            "who is",
            "what is",
            "when did",
            "where is"
        ]
    ):
        return "search"

    # internal knowledge
    return "rag"