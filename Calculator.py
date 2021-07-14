# //create a calculator by using class in python


# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
# Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
# Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string


# Solution:

class cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

a = int(input('Enter First number : '))
b = int(input('Enter Second number : '))        
obj=cal(a,b)
print(obj)