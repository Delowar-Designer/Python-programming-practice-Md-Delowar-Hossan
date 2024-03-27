# elif, neated if, else in python
'''
naumber1 = int(input("Enter value of Number1: "))
naumber2 = int(input("Enter value of Number2: "))
if naumber1 > naumber2:
    print("naumber1 is big")

elif naumber1 == naumber2:
    print("naumber1 and number2 is equal")
else:
    print("naumber2 is big")


a = input("a = ")
b = input("b = ")
c = input("c = ")

if a > b:
    if a > c:
        print("a is big")
    else:
        print("c is big")
elif b > c:
    print("b is big")
else:
    print("c is big")
'''
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a>b and a>c:
    print("a is big")

elif b>c and b>a:
    print("b is big")

else:
    print("c is big")