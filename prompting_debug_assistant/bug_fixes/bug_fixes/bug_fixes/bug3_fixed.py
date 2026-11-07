def calculate_average(numbers):
    """Ədədlər siyahısının ədədi ortasını hesablayır."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    # Test Case 1
    nums = [10, 20, 30, 40]
    expected = 25.0
    actual = calculate_average(nums)
    assert actual == expected, f"Gözlənilən {expected}, amma alınan {actual}"
    print(f"Bug 3 Test Passed: Output {actual} ✅")
