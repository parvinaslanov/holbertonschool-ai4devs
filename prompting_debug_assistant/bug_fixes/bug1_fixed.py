def get_last_n_elements(lst, n):
    """
    Returns the last n elements from the given list.
    Handles non-positive integer bounds gracefully.
    """
    if n <= 0:
        return []
    return lst[-n:]


if __name__ == "__main__":
    # Test case validation for Bug 1
    input_list = [1, 2, 3, 4, 5]
    n_val = 3
    expected_output = [3, 4, 5]
    actual_output = get_last_n_elements(input_list, n_val)
    
    assert actual_output == expected_output, f"Expected {expected_output}, got {actual_output}"
    print("Bug 1 validation test passed successfully! ✅")
