def append_to_cache(item, cache=None):
    """
    Intended: Append an item to a fresh cache list by default if no list is provided.
    Fix: Use None as default value and instantiate a new list inside the call.
    """
    if cache is None:
        cache = []
    cache.append(item)
    return cache


def parse_user_age(user_dict):
    """
    Intended: Access the user's age securely from a dynamic dictionary.
    Fix: Use .get() method with a default fallback to avoid KeyError.
    """
    return user_dict.get("age", None)


if __name__ == "__main__":
    print("Cache 1:", append_to_cache("A"))
    print("Cache 2:", append_to_cache("B"))
    
    user_info = {"name": "Bob"}
    print("Age:", parse_user_age(user_info))
