def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

scores = [78, 85, 92, 66]
print(calculate_average(scores))
print(calculate_average([]))
