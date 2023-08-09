# Class: A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that objects of that class will have. Here's an example of a simple class in Python:


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")


















# Inheritance: Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). It promotes code reusability and supports the concept of hierarchy. Here's an example:

class ElectricCar(Car):
    def charge(self):
        print(f"The {self.brand} {self.model} is charging.")

electric_car = ElectricCar("Tesla", "Model S")
electric_car.drive()   # Inherited from the Car class
electric_car.charge()  # Defined in the ElectricCar class



# Encapsulation: Encapsulation is the practice of hiding internal details and providing a public interface to interact with objects. It helps in achieving data abstraction and protection. In Python, you can achieve encapsulation by using naming conventions and access modifiers (such as _ and __). Here's an example:


class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")
    
    def get_balance(self):
        return self.__balance
    

# Polymorphism: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables code flexibility and extensibility. In Python, polymorphism is achieved through method overriding and method overloading. Here's an example:


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

def print_area(shape):
    print(f"The area is: {shape.area()}")

rectangle = Rectangle(4, 5)
circle = Circle(3)

print_area(rectangle)  # Output: The area is: 20
print_area(circle)     # Output: The area is: 28.26
