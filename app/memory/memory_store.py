# app/memory/memory_store.py

conversation_history = {}


def add_message(
    session_id,
    role,
    content
):

    if session_id not in conversation_history:

        conversation_history[
            session_id
        ] = []

    conversation_history[
        session_id
    ].append(
        {
            "role": role,
            "content": content
        }
    )


def get_history(
    session_id
):

    return conversation_history.get(
        session_id,
        []
    )


def clear_history():

    conversation_history.clear()


def get_last_messages(
    limit: int = 10
):

    return conversation_history[-limit:]