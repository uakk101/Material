def calculate_average(numbers):
    if not numbers:
        return 0  # Return 0 if the list is empty to avoid division by zero
    return sum(numbers) / len(numbers)

# Demonstration:
numbers_list = [1, 2, 3, 4, 5]
average = calculate_average(numbers_list)
print("Average of the list:", average)
