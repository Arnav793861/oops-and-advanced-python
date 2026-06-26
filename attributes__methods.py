class Animal:
    a =12 #class attribute

    def __init__(self,name):
        self.name =name #object / instance attribute
    def hello(self):# instance method / object method
        print("how are you") 

obj = Animal("lion")
obj.hello()