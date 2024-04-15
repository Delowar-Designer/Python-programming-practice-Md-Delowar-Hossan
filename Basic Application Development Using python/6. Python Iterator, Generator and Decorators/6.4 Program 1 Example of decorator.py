# Example of decorator
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

decorated_ffunction = my_decorator(print_text)
decorated_ffunction()