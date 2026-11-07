def reverse_string(s):
    """Verilmiş mətni tərsinə çevirir."""
    return s[::-1]

if __name__ == "__main__":
    # Test Case 1
    input_str = "hello"
    expected = "olleh"
    actual = reverse_string(input_str)
    assert actual == expected, f"Gözlənilən {expected}, amma alınan {actual}"
    print(f"Bug 2 Test Passed: Output '{actual}' ✅")
