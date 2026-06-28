class Animal:#parent class
    a =12
    def __init__(self,name):
       self.name=name
    def deatils(self):
        print(f"hello your name is {self.name}")

class Humans(Animal):#child class
    pass
obj =Animal("lion")

obj2 = Humans("arnav")

obj2.deatils()

print(obj2.a)

''' your child class objects has all the powers to access the
attribute and method of parent class'''
#single level inheritance

class Bagfactory:
    def __init__(self,material,zip,pockets):
        self.material = material
        self.zip = zip
        self.pockets = pockets
    def details(self):
        print("Your bag details are:")
        print(self.material)
        print(self.zip)
        print(self.pockets)
class Reebook(Bagfactory):
    def __init__(self, material, zip, pockets,color):
        super().__init__(material, zip, pockets)
        self.color = color
    def details(self):
        print(self.color)
        return super().details() 
       

bag1 = Bagfactory("leather",3,4)
bag2 =Reebook("polyester",4,2,"orange")

bag2.details()

# multi level inheritance

class Bagfactory:
    def __init__(self,material,zip,pockets):
        self.material = material
        self.zip = zip
        self.pockets = pockets
    def details(self):
        print("Your bag details are:")
        print(self.material)
        print(self.zip)
        print(self.pockets)
class Reebook(Bagfactory):
    def __init__(self, material, zip, pockets,color):
        super().__init__(material, zip, pockets)
        self.color = color
    def details(self):
        print(self.color)
        return super().details() 
class Campus(Reebook):
    def __init__(self, material, zip, pockets, color,price):
        super().__init__(material, zip, pockets, color)
        self.price = price
    def details(self):
        print(self.price)
        return super().details()
       

bag1 = Bagfactory("leather",3,4)
bag2 =Reebook("polyester",4,2,"orange")
bag3 = Campus("wollen",2,3,"grey",2345)

bag2.details()
bag3.details()

# multiple inheritance

class Animal:
    def __init__(self, name):
        self.name = name


class Humans:
    def __init__(self, id):
        self.id = id


class Robot(Animal, Humans):
    def __init__(self, name, id):
        Animal.__init__(self, name)
        Humans.__init__(self, id)


robo = Robot("arnav", 2547021)

print(robo.name)
print(robo.id)