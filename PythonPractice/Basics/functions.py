


# def greet():
#     print("Hello, world!")

# greet()



# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 3)
# print(result)




# import math

# result = math.sqrt(16)
# print(result)



# from random import randint

# random_number = randint(1, 100)
# print(random_number)





# def greet(name):
#     print("Hello, " + name + "!")




# import mymodule

# mymodule.greet("Alice")

# def greet(name, message="Hello"):
#     print(f"{message}, {name}!")


# greet("John")  
# greet("Emily" , "Hi")  

# pass by value and pass by reference:


def update_list(lst):
    lst.append(4)  # Modifying the list

def update_number(num):
    num += 1  # Modifying the number
    print(num)

my_list = [1, 2, 3]
update_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

my_number = 10
update_number(my_number)
print(my_number)  # Output: 10 (unchanged)


# Recursive Functions

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function
result = factorial(5)
print(result)  







