# Write a Program to find big number among three in python using class
class bignumber:
    def big(g,a,b,c):
        if(a>b and a>c):
            print("Big Number is:",a)
        elif(b>a and b>c):
            print("Big Number is:",c)
        else:
            print("Big Number is:",c)

a = int(input("Enter the 1st number = "))
b = int(input("Enter the 2nd number = "))
c = int(input("Enter the 3rd number = "))
x = bignumber()
x.big(a,b,c)

