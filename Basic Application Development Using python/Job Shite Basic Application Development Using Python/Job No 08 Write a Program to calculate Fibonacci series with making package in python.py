# Write a Program to calculate Fibonacci series with making package in python
# Lets create a package named mypackage, using the following steps:
    # create a new folder named D:/MyApp.
    # inside My App, create a subfolder with the name 'mypackage'
    # Create an empty_init_.py file in the mypackage folder.
    # Usig a Python-aware editor like IDLE,greate modules testfib.py with the following cod:



def fib(n):
    a = 0
    b = 1
    if n == 1:
        return a
    else:
        return a
        return b
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        return c
#from mypackage inport testfibo
n = int(input("Enter how many terms:"))
x = fib(n)
print(x)