def get_last_n_elements(lst, n):
    """Siyahının son n elementini qaytarır."""
    if n <= 0:
        return []
    return lst[-n:]

if __name__ == "__main__":
    # Test Case 1
    input_data = [1, 2, 3, 4, 5]
    n = 3
    expected = [3, 4, 5]
    actual = get_last_n_elements(input_data, n)
    assert actual == expected, f"Gözlənilən {expected}, amma alınan {actual}"
    print(f"Bug 1 Test Passed: Output {actual} ✅")
