def get_last_n_elements(lst, n):
    """Siyahının son n elementini qaytarır."""
    if n <= 0:
        return []
    return lst[-n:]

if __name__ == "__main__":
    # Test case
    input_data = [1, 2, 3, 4, 5]
    n_val = 3
    expected = [3, 4, 5]
    actual = get_last_n_elements(input_data, n_val)
    assert actual == expected, f"Expected {expected}, got {actual}"
    print(f"Bug 1 Passed: Output {actual} ✅")
