# class Car():
#    speed = 10

# toyota = Car()


# print(toyota.speed) # 10

# Car.speed = 20 # change the class attribute will update all the objects of that class

# print(toyota.speed) # 20






# # we use double _ _ to make it private

# class Car():
#     def __init__(self, speed):
#         # this stops us from accessing the __height
#         # property directly on an instance of a Wall
#         self.__speed = speed

#     def get_speed(self):
#         return self.__speed
    

# toyota = Car(40)

# print(toyota.get_speed())

    
# This will prevent us from accessing the __height property directly

# ------------------------------------------------------------------------Inheritance-----------------------------------------------
# class Animal:
#     def __init__(self, num_legs):
#         self.num_legs = num_legs

# class Cow(Animal):
#     def __init__(self):
#         # call the parent constructor to
#         # give the cow some legs
#         super().__init__(4)

# ==================================================================Polymorphism=========================================================


class Creature():
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")

class Kraken(Creature):
    def move(self):
        print("the kraken swims")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# prints:
# the creature moves
#  dragon fliesthe
# the kraken swims


#  ---------------------------------------------Operator Overloading -----------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# p1 = Point(4, 5)
# p2 = Point(2, 3)
# p3 = p1 + p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
# ===========================================================================
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, point):
#         x = self.x + point.x
#         y = self.y + point.y
#         return Point(x, y)

# p1 = Point(4, 5)
# p2 = Point(2, 3)
# p3 = p1 + p2
# # p3 is (6, 8)

# When you call p1 + p2 under the hood the interpreter just calls p1.__add__(p2).


# # ===========================================================================__Raper__=====================================
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"({self.x},{self.y})"

# p1 = Point(4, 5)
# print(p1)
# # prints "(4,5)"