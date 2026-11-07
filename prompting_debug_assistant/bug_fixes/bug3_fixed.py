def calculate_average(numbers):
    """Ədədlər siyahısının ədədi ortasını hesablayır."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    # Test case
    input_nums = [10, 20, 30, 40]
    expected = 25.0
    actual = calculate_average(input_nums)
    assert actual == expected, f"Expected {expected}, got {actual}"
    print(f"Bug 3 Passed: Output {actual} ✅")
