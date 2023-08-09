def remove_duplicates(numbers_list):
    unique_list = []
    for number in numbers_list:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list


input_numbers = input("Enter a list of integers separated by spaces: ")
my_list = [int(num) for num in input_numbers.split()]
result = remove_duplicates(my_list)
print("List without duplicates:", result)





# def main():
#     # Taking input from the user for the list of integers
   

#     # Converting the input string into a list of integers
#     try:
        
#     except ValueError:
#         print("Invalid input. Please enter a valid list of integers.")

# if __name__ == "__main__":
#     main()
