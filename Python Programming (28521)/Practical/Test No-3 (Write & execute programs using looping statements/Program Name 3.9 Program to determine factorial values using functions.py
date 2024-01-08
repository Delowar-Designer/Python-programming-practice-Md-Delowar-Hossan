# Program to determine factorial values using functions
def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact*i
        i = i + 1
    return fact
n = int(input("Enter Number of Factorial Value = "))
print(n,"Factorial Valua = ",factorial(n))