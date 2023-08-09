

fruits = ("apple", "banana", "cherry")


print(fruits[0])  # Output: apple




# This will raise an error because tuples are immutable
fruits[0] = "orange"


fruits = ("apple", "banana", "cherry")
more_fruits = ("orange", "grape", "kiwi")
all_fruits = fruits + more_fruits
print(all_fruits)  # Output: ('apple', 'banana', 'cherry', 'orange', 'grape', 'kiwi')


numbers = (1, 2, 3, 2, 1, 2, 3, 1, 1)
count_of_ones = numbers.count(1)
print(count_of_ones)  # Output: 4


fruits = ("apple", "banana", "cherry", "banana")
banana_index = fruits.index("banana")
print(banana_index)  # Output: 1
