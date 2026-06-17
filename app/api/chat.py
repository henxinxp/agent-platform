from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.agent_graph import agent

from app.memory.memory_store import (
    add_message
)


router = APIRouter()


class ChatRequest(BaseModel):

    session_id: str

    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    # 保存用户消息
    add_message(
        request.session_id,
        "user",
        request.question
    )

    result = agent.invoke(
        {
            "session_id": request.session_id,
            "question": request.question
        }
    )

    answer = result["answer"]

    # 保存AI回复
    add_message(
        request.session_id,
        "assistant",
        answer
    )

    return {
        "question": request.question,
        "answer": answer
    }