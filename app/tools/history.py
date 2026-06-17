from app.memory.memory_store import (
    get_history
)


def show_history():

    history = get_history()

    if not history:
        return "No conversation history."

    text = ""

    for item in history:

        text += (
            f"{item['role']}: "
            f"{item['content']}\n"
        )

    return text