from app.memory.user_profile import *

profile = load_profile()

profile["name"] = "Wei"

save_profile(profile)

print(
    load_profile()
)