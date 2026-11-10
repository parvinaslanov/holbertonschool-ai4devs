def append_to_cache(item, cache=[]):
    """
    Intended: Append an item to a fresh cache list by default if no list is provided.
    """
    # Bug: Mutable default argument retains state across multiple function invocations
    cache.append(item)
    return cache


def parse_user_age(user_dict):
    """
    Intended: Access the user's age securely from a dynamic dictionary.
    """
    # Bug: KeyError triggered when accessing missing key directly instead of using .get()
    return user_dict["age"]


if __name__ == "__main__":
    print("Cache 1:", append_to_cache("A"))
    print("Cache 2:", append_to_cache("B"))  # Unexpectedly contains ['A', 'B']

    user_info = {"name": "Bob"}
    print("Age:", parse_user_age(user_info))
