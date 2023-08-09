

# The __init__ method is a special method in Python classes that is automatically called when an object is created from the class. It is known as the constructor method. The purpose of __init__ is to initialize the object's attributes or properties.


# In the given code snippet, the __init__ method takes two parameters: brand and model. These parameters represent the brand and model of a car. Within the method, the self keyword refers to the instance of the class being created. By using the self keyword, we can assign the passed values to the object's attributes.


class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

Toyota = Car("Toyota", "Corolla" , "red")


print(Toyota.brand)  # Output: Toyota
print(Toyota.model)  # Output: Corolla
print(Toyota.color)  # Output: red

car2 = Car("Honda", "Civic")
print(car2.brand)  # Output: Honda
print(car2.model)  # Output: Civic
