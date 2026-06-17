import json
import os

MEMORY_FILE = "memory.json"


def load_profile():

    if not os.path.exists(
        MEMORY_FILE
    ):
        return {}

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def save_profile(profile):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            profile,
            f,
            indent=2
        )