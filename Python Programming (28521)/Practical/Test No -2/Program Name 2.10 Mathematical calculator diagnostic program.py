# Mathematical calculator diagnostic program
# https://www.geeksforgeeks org/make-simple-calculator-using-python/
# Python Program for simple calculator
# Function to add two numbers
def add(num1,num2):
    return num1+num2

# Function to subtract two numbers
def subtract(num1,num2):
    return num1-num2

# Function to multiply two numbers
def multiply(num1,num2):
    return num1*num2

# Function to divide two numbers
def divide(num1,num2):
    return num1/num2

print("Pleade select Operation -\n"\
      "1. Addition\n"\
      "2. Subtraction\n"\
      "3. Multiplication\n"\
      "4. Division\n")

# Take input From the user
Selct = int(input("Select Operations form 1, 2, 3, 4: "))
if Selct>4 or Selct<=0:
    print("Invalid Selection, Pleade Try Again")
else:
    number_1 = int(input("Enter First Number: "))
    number_2 = int(input("Enter Second Number: "))

    if Selct==1:
        print(number_1,"+",number_2,"=",add(number_1,number_2))

    elif Selct==2:
        print(number_1,"-",number_2,"=",subtract(number_1,number_2))

    elif Selct==3:
        print(number_1,"*",number_2,"=",multiply(number_1, number_2))

    elif Selct==4:
        print(number_1,"/",number_2,"=",divide(number_1,number_2))

    print("======================================")



