def countdown(start):
    """
    Intended Behavior: Print numbers counting down from start to 1.
    Issue Type: Logical error / Infinite loop
    """
    current = start
    while current > 0:
        print(current)
        current -= 1

# Test case
# countdown(5)
