def my_dec(func):
    def wrap():
        print("##############################")
        func()
        print("##############################")
    return wrap


@my_dec
def greet():
    print("Good evening, Ravindra")
    
greet()