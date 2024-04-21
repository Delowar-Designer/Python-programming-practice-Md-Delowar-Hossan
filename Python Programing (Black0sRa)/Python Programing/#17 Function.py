# Function
def myFunc(name,):
    print(f"{name}, i am from MyFunc")

myFunc("Mitu")
myFunc("Joty")

def myFunction(name = "Delowar"):
    print(f"Hello {name}, you are the winner")
myFunction()
myFunction("Joty")

def add (num1, num2):
    print(f"add: {num1+num2}")
    print(f"mul: {num1*num2}")

add(2,4)

def add(num1, num2):
    return num1+num2
print(add(4,5))

def myFunction(first_name, second_name):
    print(f"First Name: {first_name}, Second Name: {second_name}")
myFunction("Saon","Joty")