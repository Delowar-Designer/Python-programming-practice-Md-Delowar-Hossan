# Program to find the largest number between two numbers using functions
def Largest():
    Number1 = int(input("Enter the value of 1st Number: "))
    Number2 = int(input("Enter the value of 2nd Number: "))
    if(Number1>Number2):
        print("Largest is Numbdr1 & it is = ",Number1)
    else:
        print("Largest is Number2 & it is= ",Number2)
Largest()