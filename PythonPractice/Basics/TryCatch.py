
try:
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

finally:
    print("Execution completed.")




# try:
#     result = "5" + 3
# except TypeError as e:
#     print("An error occurred:", str(e))



# try:
#     numbers = [1, 2, 3]
#     print(numbers[3])
# except IndexError as e:
#     print("An error occurred:", str(e))



# try:
#     data = {"name": "John", "age": 25}
#     print(data["gender"])
# except KeyError as e:
#     print("An error occurred:", str(e))



# try:
#     import nonexistingmodule
# except ImportError as e:
#     print("An error occurred:", str(e))

