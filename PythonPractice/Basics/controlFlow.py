



for i in range(1, 6):
    if i == 3:
        continue
    print(i)


#output

#1
#2
#4
#5



for i in range(1, 6):
    if i == 3:
        break
    print(i)
#output
#1
#2


for i in range(1, 6):
    if i == 3:
        pass
    print(i)

#1
#2
#4
#3
#5


