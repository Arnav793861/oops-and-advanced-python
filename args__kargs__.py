def addition(*args):
    s=0
    for i in args:
        s=s+i
    return s
print(addition(20,30,50,67,56,78,34))

def info(**kwargs):
    return kwargs
print(info(name="arnav",age=20,profession="Data Scientist"))
def extragreeting(func):
    def wrapper(*args,**kwargs):
        print("hello from the arnav thakur")
        func(*args,**kwargs)
        print("thankyou visit again")
    return wrapper
@extragreeting
def addition(a,b,c):
    print(a+b+c)

addition(10,20,30)