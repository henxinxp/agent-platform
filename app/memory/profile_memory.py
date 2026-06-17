# app/memory/profile_store.py

profile = {}

def set_profile(key, value):
    profile[key] = value

def get_profile(key):
    return profile.get(key)

def get_all_profile():
    return profile