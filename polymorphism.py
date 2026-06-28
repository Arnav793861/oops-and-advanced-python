class Animal:
    def hello(self):
        print("animals do not say hello")
class Human:
    def hello(self):
        print("human can say hello")

obj = Animal()
obj2 =Human()

obj.hello()
obj2.hello()

#METHOD OVERIDING{WE NEED INHERITANCE TO ACHIEVE IT}

class Animal:
    a=12
    def __init__(self,name):
        self.name = name
    def details(self):
        print(f"the name is {self.name}")
class Human(Animal):
    b=12
    def details(self):
        print(f"the human name is {self.name}")

obj = Human("arnav")
obj.details()