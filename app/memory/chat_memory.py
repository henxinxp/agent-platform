memory = []


def add_message(
    role: str,
    content: str
):

    memory.append(
        {
            "role": role,
            "content": content
        }
    )


def get_history():

    return memory