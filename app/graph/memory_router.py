from app.memory.profile_agent import recall

def memory_check(question: str):

    result = recall(question)

    if result:
        return result

    return None