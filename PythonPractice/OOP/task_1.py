def calculate_sum(numbers_list):
    total_sum = 0
    for number in numbers_list:
        total_sum += number
    return total_sum

input_numbers = input("Enter a list of numbers separated by spaces: ")

numbers_list = [int(num) for num in input_numbers.split()]
result = calculate_sum(numbers_list)
print("Sum of the numbers:", result)






# def main():
#     # Taking input from the user for the list of numbers
#     input_numbers = input("Enter a list of numbers separated by spaces: ")

#     # Converting the input string into a list of integers
#     try:
#         numbers_list = [int(num) for num in input_numbers.split()]
#         result = calculate_sum(numbers_list)
#         print("Sum of the numbers:", result)
#     except ValueError:
#         print("Invalid input. Please enter a valid list of numbers.")

# if __name__ == "__main__":
#     main()
