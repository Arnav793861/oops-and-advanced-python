class Bags:
    def __init__(self,material,zip,pockets):# automaticaly awakes when we call a class
          self.material=material
          self.zip=zip
          self.pockets=pockets

reebok = Bags("leather",3,2)
campus =Bags("polyster",2,4)

print(reebok.material,campus.material)