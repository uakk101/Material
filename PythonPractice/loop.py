my_list = [1, 2, 3, 4, 5]

my_list2 = [i ** 2 for i in my_list]

print(my_list2)


# Touple 

touple = (1, 2, 3, 4, 5)

my_touple2 = ([1,2,3,4,5])

for i in my_touple2:
    print(i)


if 1 in my_touple2:
    print("yes")
else:
    print("no")

print(len(my_touple2))

print(my_touple2.count(2))

print(my_touple2.index(2))

my_list3 = list(touple)

my_touple3 = tuple(my_list3)

print(my_touple3[2:4])  # slicing in touples


for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')





















    rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')









