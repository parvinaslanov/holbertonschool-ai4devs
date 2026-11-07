def reverse_string(s):
    """Verilmiş mətni tərsinə çevirir."""
    return s[::-1]

if __name__ == "__main__":
    # Test case
    input_str = "hello"
    expected = "olleh"
    actual = reverse_string(input_str)
    assert actual == expected, f"Expected {expected}, got {actual}"
    print(f"Bug 2 Passed: Output '{actual}' ✅")
