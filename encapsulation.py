class Factory:
    name ="kia" #PUBLIC CLASS ATTRIBUTE
    _old =12    #PROTECTED
    __marks =67  #PRIVATE
    def __init__(self,type,tyre,color,seater):
        self.type = type #PUBLIC OBJECT ATTRIBUTR
        self.tyre = tyre
        self.color =color
        self.__seater =seater #PRIVATE OBJECT ATTRIBUTE
    def detail(self):#PUBLIC METHOD
        print(f"type:{self.type}")
        print(f"tyre:{self.tyre}")
        print(f"color:{self.color}")
        print(f"seater:{self.__seater}")
# for method also just put __ in the begining it will be private method
'''def __detail(self):  #PRIVATE METHOD IT WILL NOT ACESSED OUTSIDE THE CLASS
        print(f"type:{self.type}")
        print(f"tyre:{self.tyre}")
        print(f"color:{self.color}")
        print(f"seater:{self.__seater}")''' 


obj = Factory("sedan","mrf","black",9)

obj.name = "maruti"

print(obj.name)
obj.detail()
obj.__marks =89
#print(obj.marks)# since it is private it will show error outside the class
obj.seater =7 #hence it is private it can not be acessed outside the class
obj.detail()

'''SO THE QUESTION ARISE IS THERE ANY WAY TO ACESS IT 
   YES THERE IS A WAY BUT GENERALLY IT IS NOT NEEDED'''
#EXAMPLE FOR UNDERSTANDING

class School:
    __location ="chandigarh"#private 
    @classmethod
    def magic(cls):
        print(cls.__location)

xyz = School()
School.magic()