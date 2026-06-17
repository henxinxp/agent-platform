# app/memory/profile_store.py

profile = {}


def set_profile(
    key: str,
    value: str
):

    profile[key] = value


def get_profile(
    key: str
):

    return profile.get(key)


def get_all_profile():

    return profile


def clear_profile():

    profile.clear()