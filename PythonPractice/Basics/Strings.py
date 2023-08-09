# len(): Returns the length of the string.
string = "Hello, World!"
length = len(string)
print(length)  # Output: 13



# lower(): Converts the string to lowercase.
string = "Hello, World!"
lowercase_string = string.lower()
print(lowercase_string)  # Output: hello, world!


# upper(): Converts the string to uppercase.
string = "Hello, World!"
uppercase_string = string.upper()
print(uppercase_string)  # Output: HELLO, WORLD!


# capitalize(): Converts the first character of the string to uppercase and the rest to lowercase.

string = "hello, world!"
capitalized_string = string.capitalize()
print(capitalized_string)  # Output: Hello, world!


# title(): Converts the first character of each word in the string to uppercase and the rest to lowercase.

string = "hello, world!"
title_string = string.title()
print(title_string)  # Output: Hello, World!


# strip(): Removes leading and trailing whitespace from the string.
string = "   Hello, World!   "
stripped_string = string.strip()
print(stripped_string)  # Output: Hello, World!


# split(): Splits the string into a list of substrings based on a specified delimiter.
string = "Hello, World!"
split_list = string.split(", ")
print(split_list)  # Output: ['Hello', 'World!']


# join(): Joins elements of a list into a string using a specified delimiter.

list_of_words = ['Hello', 'World!']
joined_string = ", ".join(list_of_words)
print(joined_string)  # Output: Hello, World!


# replace(): Replaces all occurrences of a specified substring with another substring.
string = "Hello, World!"
new_string = string.replace("Hello", "Hi")
print(new_string)  # Output: Hi, World!


# startswith(): Checks if the string starts with a specified substring.

string = "Hello, World!"
starts_with_hello = string.startswith("Hello")
print(starts_with_hello)  # Output: True
