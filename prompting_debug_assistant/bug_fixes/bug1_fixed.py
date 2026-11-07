def get_last_n_elements(lst, n):
    """Siyahının son n elementini qaytarır."""
    if n <= 0:
        return []
    return lst[-n:]

if __name__ == "__main__":
    assert get_last_n_elements([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    print("Bug 1 Test Passed ✅")
