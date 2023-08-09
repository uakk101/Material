



fruits = ["apple", "banana", "cherry"]


print(fruits[0])  # Output: apple



fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "grape")
print(fruits)  # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']




fruits.remove("banana")
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'orange']


numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]



fruits.reverse()
print(fruits)  # Output: ['orange', 'cherry', 'grape', 'apple']


numbers = [1, 2, 3, 2, 1, 2, 3, 1, 1]
count_of_ones = numbers.count(1)
print(count_of_ones)  # Output: 4
