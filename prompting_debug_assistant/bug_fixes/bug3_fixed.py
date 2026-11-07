def calculate_average(numbers):
    """
    Calculates the average of numbers in a list.
    Returns 0.0 if the input list is empty.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # Test case validation for Bug 3
    input_numbers = [10, 20, 30, 40]
    expected_output = 25.0
    actual_output = calculate_average(input_numbers)
    
    assert actual_output == expected_output, f"Expected {expected_output}, got {actual_output}"
    print("Bug 3 validation test passed successfully! ✅")
