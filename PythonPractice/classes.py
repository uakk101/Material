

class Calculator:
    name = "usman"
    id = 9000
    def __init__(self, num1:float, num2:float):
        assert num2 >=0  , "Please Enter positive number"
        assert num1 >=0  , "Please Enter positive number"

        self.num1 = num1
        self.num2 = num2
    def add(self):
       return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        if self.num2 == 0:
            return "Error"
        else:
            return self.num1 / self.num2

print(Calculator.name)










