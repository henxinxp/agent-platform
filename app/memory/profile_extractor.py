import re

from app.memory.profile_store import set_profile

def extract_profile(text):

    m = re.search(
        r"my name is (.+)",
        text,
        re.I
    )

    if m:

        set_profile(
            "name",
            m.group(1).strip()
        )

    m = re.search(
        r"i study at (.+)",
        text,
        re.I
    )

    if m:

        set_profile(
            "university",
            m.group(1).strip()
        )

    m = re.search(
        r"i live in (.+)",
        text,
        re.I
    )

    if m:

        set_profile(
            "city",
            m.group(1).strip()
        )