# Bug 1: Calculate the average of a list of numbers.
def calculate_average(numbers):
    if len(numbers) == 0
        return 0
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

scores = [78, 85, 92, 66]
print("Average:", calculate_average(scores))
