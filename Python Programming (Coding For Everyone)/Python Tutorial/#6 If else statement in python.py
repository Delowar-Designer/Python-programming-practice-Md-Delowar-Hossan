#6 If else statement in python
a = 8
b =8
c = 8

if a>9:
    print("a is greater than")
elif b>9:
    print("b is greater than")
elif c>10:
    print("c is greater than")
else:
    print("a and b is less than")

a = 11
b = 9

if a>10:
    print("a is greater than")
    if b>10:
        print("b is greater than")
    else:
        print("b is less than")
else:
    print("a is not greater than")
