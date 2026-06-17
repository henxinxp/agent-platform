from app.memory.user_profile import (
    load_profile,
    save_profile
)


def remember(question: str):

    profile = load_profile()

    q = question.lower()

    if "my name is" in q:

        name = question.split(
            "My name is"
        )[1].strip()

        profile["name"] = name

        save_profile(profile)

        return "Name saved."

    if "i study at" in q:

        school = question.split(
            "I study at"
        )[1].strip()

        profile["university"] = school

        save_profile(profile)

        return "University saved."

    return None

def recall(question: str):

    profile = load_profile()

    q = question.lower()

    if "what is my name" in q:

        return (
            f"Your name is "
            f"{profile.get('name','Unknown')}."
        )

    if "where do i study" in q:

        return (
            f"You study at "
            f"{profile.get('university','Unknown')}."
        )

    return None