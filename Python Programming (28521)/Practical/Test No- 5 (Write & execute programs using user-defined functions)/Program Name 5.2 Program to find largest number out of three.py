# Program to find largest number out of three numbers using function passing arguments
def max3val(x,y,z):
    if(a > b) and (a > c):
        print("A is maximum: ",a)
    elif(b>c):
        print("B is maximum: ",b)
    else:
        print("C is maximum: ",c)
a = int(input("Enter first Number = "))
b = int(input("Enter second Number = "))
c = int(input("Enter third Number = "))
max3val(a,b,c)