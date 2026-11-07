def countdown(start):
    """
    Intended Behavior: Print numbers counting down from start to 1.
    Issue Type: Logical error / Infinite loop
    """
    current = start
    while current > 0:
        print(current)
        # Bug: Incrementing instead of decrementing causes an infinite loop
        current += 1 

# Example usage:
# countdown(5)
