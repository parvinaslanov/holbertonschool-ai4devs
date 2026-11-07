def reverse_string(s):
    """
    Reverses the given string input.
    Returns empty string if the input string is empty.
    """
    if not s:
        return ""
    return s[::-1]


if __name__ == "__main__":
    # Test case validation for Bug 2
    input_text = "hello"
    expected_output = "olleh"
    actual_output = reverse_string(input_text)
    
    assert actual_output == expected_output, f"Expected {expected_output}, got {actual_output}"
    print("Bug 2 validation test passed successfully! ✅")
