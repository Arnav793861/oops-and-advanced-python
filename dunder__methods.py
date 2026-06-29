#dunder methods

class Animal:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"hello my name is {self.name}"

obj = Animal("lion")
obj2= Animal("fox")

print(obj)
print(obj2)

class Numbers:
    def __init__(self,num):
        self.num =num
    def __add__(self,other):
        return self.num + other.num
    def __eq__(self,value):
        return self.num ==value.num

num1 = Numbers(30)
num2 = Numbers(30)

print(num1+num2)

print(num1==num2)