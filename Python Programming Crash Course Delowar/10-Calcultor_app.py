# ----Calculator app in python---


# function create
def addition(num1, num2):
    result = num1 + num2  # num1-value+num2-value=result
    print("{0} + {1} = {2}".format(num1, num2, result))


def substraction(num1, num2):
    result = num1 - num2  # num1-value-num2-value=result
    print("{0} - {1} = {2}".format(num1, num2, result))


def multiplication(num1, num2):
    result = num1 * num2  # num1-value*num2-value=result
    print("{0} * {1} = {2}".format(num1, num2, result))


def division(num1, num2):
    if num2 == 0.0:
        print("cant do divide by zero")
    else:
        result = num1 / num2  # num1-value/num2-value=result
        print("{0} / {1} = {2}".format(num1, num2, result))

while True:

# display
    print("What do you want to do?")
    print("1 for addition")
    print("2 for substraction")
    print("3 for multiplication")
    print("4 for division")
    print("Enter Q OR q to Exit the calculator")
# user input -2 digit number
    choice = input("Enter your Choice: ")
    if choice == 'Q' or choice == 'q':
        break
# taking a 2 number as a input form user
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))
# Condition
    if choice == "1":
        addition(num1, num2)
    elif choice == "2":
        substraction(num1, num2)
    elif choice == "3":
        multiplication(num1, num2)
    elif choice == "4":
        division(num1, num2)
    else:
        print("Invalid Choice")
