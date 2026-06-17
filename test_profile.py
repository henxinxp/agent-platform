from app.memory.profile_agent import remember

print(
    remember(
        "My name is Wei"
    )
)

print(
    remember(
        "I study at TMU"
    )
)


from app.memory.profile_agent import recall

print(
    recall(
        "What is my name?"
    )
)

print(
    recall(
        "Where do I study?"
    )
)