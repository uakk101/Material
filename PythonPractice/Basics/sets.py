

my_set = {1, 2, 3, 4, 5}
print(my_set)

# {1, 2, 3, 4, 5}


my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)

# {1, 3, 4}

my_frozen_set = frozenset([1, 2, 3, 4])
print(my_frozen_set)

# frozenset({1, 2, 3, 4})


my_dict = {frozenset([1, 2, 3]): 'value'}
print(my_dict)


# {frozenset({1, 2, 3}): 'value'}



