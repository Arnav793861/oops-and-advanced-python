def extragreeting(func):
    def wrapper():
        print("hello from the arnav thakur")
        func()
        print("thankyou visit again")
    return wrapper

@extragreeting
def greetings():
    print("good morning")

greetings()