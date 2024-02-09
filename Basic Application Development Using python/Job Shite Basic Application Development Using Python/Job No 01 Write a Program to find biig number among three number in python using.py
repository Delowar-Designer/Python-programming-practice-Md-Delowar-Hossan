# Write a Program to find biig number among three number in python using
def big():
    a = int(input("Enter the 1st number= "))
    b = int(input("Enter the 2nd number= "))
    c = int(input("Enter the 3rd number= "))
    if(a>b and b>c):
        print("Big Number is: ",a)
    elif(b>a and b>c):
        print("Big Number is: ",b)
    else:
        print("Big Number is: ",c)
big()