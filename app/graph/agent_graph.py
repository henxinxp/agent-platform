from langgraph.graph import StateGraph
from langgraph.graph import START, END

from app.graph.state import AgentState

from app.tools.calculator import calculate
from app.tools.weather import get_weather
from app.tools.search import search_web

from app.rag.rag_agent import ask_rag

from app.graph.router_llm import choose_tool
from app.graph.memory_router import memory_check


# -------------------------
# Router
# -------------------------

def router(state: AgentState):

    memory_result = memory_check(
        state["question"]
    )

    if memory_result:
        return "memory"

    tool = choose_tool(
        state["question"]
    )

    print("ROUTER:", tool)

    return tool


# -------------------------
# Memory Node
# -------------------------

def memory_node(
    state: AgentState
):

    result = memory_check(
        state["question"]
    )

    return {
        "answer": result
    }


# -------------------------
# Calculator Node
# -------------------------

def calculator_node(
    state: AgentState
):

    result = calculate(
        state["question"]
    )

    return {
        "answer": result
    }


# -------------------------
# RAG Node
# -------------------------

def rag_node(
    state: AgentState
):

    result = ask_rag(
        state["session_id"],
        state["question"]
    )

    return {
        "answer": result
    }


# -------------------------
# Weather Node
# -------------------------

def weather_node(
    state: AgentState
):

    result = get_weather(
        state["question"]
    )

    return {
        "answer": result
    }


# -------------------------
# Search Node
# -------------------------

def search_node(
    state: AgentState
):

    result = search_web(
        state["question"]
    )

    return {
        "answer": result
    }


# -------------------------
# Build Graph
# -------------------------

graph = StateGraph(
    AgentState
)

graph.add_node(
    "memory",
    memory_node
)

graph.add_node(
    "calculator",
    calculator_node
)

graph.add_node(
    "rag",
    rag_node
)

graph.add_node(
    "weather",
    weather_node
)

graph.add_node(
    "search",
    search_node
)


# -------------------------
# Router Edges
# -------------------------

graph.add_conditional_edges(
    START,
    router,
    {
        "memory": "memory",
        "calculator": "calculator",
        "rag": "rag",
        "weather": "weather",
        "search": "search"
    }
)


# -------------------------
# End Edges
# -------------------------

graph.add_edge(
    "memory",
    END
)

graph.add_edge(
    "calculator",
    END
)

graph.add_edge(
    "rag",
    END
)

graph.add_edge(
    "weather",
    END
)

graph.add_edge(
    "search",
    END
)


print("before compile")

agent = graph.compile()

print("after compile")