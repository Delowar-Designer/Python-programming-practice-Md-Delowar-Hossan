# Return of a Function
def my_func1():
    print("Hello World")
    return None

def my_func2():
    print("Hello World")
    return

def my_func3():
    print("Hello World")


def add(a,b,c):
    return (a+b+c)
temp = add(10,25,30)
print(temp)

def add_numbers(x,y):
    total = x+y
    return total
print("This won't be printed")
print(add_numbers(15,25))
