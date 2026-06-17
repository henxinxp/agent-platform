from typing import TypedDict

class AgentState(TypedDict):

    session_id: str

    question: str

    answer: str