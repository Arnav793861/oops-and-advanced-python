from abc import ABC , abstractmethod

class enforce(ABC):
    @abstractmethod
    def enginestart():
        pass

class Bike(enforce):
    def enginestart():
        pass

class Car(enforce):
    def enginestart():
        pass

class Truck:
    pass

obj1= Bike()
obj2= Car()
obj3=Truck()
