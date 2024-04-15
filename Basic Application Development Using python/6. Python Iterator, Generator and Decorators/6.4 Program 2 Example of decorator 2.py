# Example of decorator 2
def my_decorator(func):
    def decorate():
        print("----------------------------------------------------")
        func()
        print("----------------------------------------------------")
    return decorate
print("Programer Delowar.Designer")
def print_text():
    print("Diploma in Engineering! using Decorator Funtion Example")
    print("Programer Delowar.Designer")

decorated_function = my_decorator(print_text)
decorated_function()

@my_decorator
def print_text2():
    print("Mitu are your fine")
    print("Your Famile Fine Mitu")
print_text2()

