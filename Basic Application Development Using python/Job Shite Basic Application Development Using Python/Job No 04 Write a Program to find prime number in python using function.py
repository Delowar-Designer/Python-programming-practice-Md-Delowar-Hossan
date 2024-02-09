# Write a Program to find prime number in python using function
def prime():
    n = int(input("Give the number= "))
    if(n == 0 or n == 1):
        print("F")
    else:
        for i in range(2,n):
            if(n%i==0):
                print("Not a prime number")
            print("T")
prime()