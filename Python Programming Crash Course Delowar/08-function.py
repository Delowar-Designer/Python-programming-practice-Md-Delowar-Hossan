#---- function in python ----
#--- syntax----
'''
    def function_name(Parameter):
        #code to be executed
'''
#print hello World by creating a function
#function decloration
'''
def hello_world():
    #function body
    print("Hello world")

#function calling   
hello_world()
hello_world()
hello_world()
'''
#function paramters/arguments
def hello_paramters(name):
    #function body
    A = "Hello " + name
    print(A)

#function calling   
hello_paramters("Delowar")

#Program to print addition of two numbers using finction
def add_number(num1,num2):
    sum = num1 + num2
    subtraction = num1 - num2
    division = num1 / num2
    multipilication = num1 * num2
    exponentitation = num1 ** num2
    remainder = num1 % num2
    floordivision = num1 // num2
    print(sum)
    print(subtraction)
    print(division)
    print(multipilication)
    print(exponentitation)
    print(remainder)
    print(floordivision)
add_number(10,5)

