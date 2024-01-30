# Program to find largest number out of three numbers
a = int(input("Enter the Value of a: "))
b = int(input("Enter the Value of b: "))
c = int(input("Enter the Value of c: "))
if(a>b):
    if (a>c):
        print("Largest Number is a")
    else:
        print("Largest Number is c")
else:
    if(b>c):
        print("Largest Number is b")
    else:
        print("Largest Number is c")