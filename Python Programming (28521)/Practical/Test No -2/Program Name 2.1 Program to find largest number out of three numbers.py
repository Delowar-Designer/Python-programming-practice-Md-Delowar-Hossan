# Program to find largest number out of three numbers
def max3al():
    a = int(input("Enter first Number = "))
    b = int(input("Enter Second Number = "))
    c = int(input("Enter Third Number = "))

    if(a>b and a>c):
        print("Largest number A is Maximum: ",a)

    elif(b>c):
        print("Largest number B is Maximum: ",b)

    else:
        print("Largest number C is Maximum: ",c)
max3al()
