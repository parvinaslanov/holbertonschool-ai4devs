def get_last_n_items(items, n):
    """
    Intended: Return the last n items in a list.
    """
    if n <= 0:
        return []
    # Bug: Off-by-one slicing error that excludes the first of the requested n elements
    start_index = len(items) - n + 1
    return items[start_index:]


def calculate_average(numbers):
    """
    Intended: Calculate average of non-negative numbers.
    """
    total = 0
    count = 0
    for num in numbers:
        if num >= 0:
            total += num
            count += 1
    # Bug: Potential ZeroDivisionError when input list contains no non-negative numbers
    return total / count


if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print("Last 3 items:", get_last_n_items(sample_list, 3))
    print("Average:", calculate_average([-5, -10]))
