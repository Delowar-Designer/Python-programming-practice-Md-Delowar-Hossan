# Write a Program to calculate factorial value with making module in pyghon
'''def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))

# seve this program as testfact

import testfact
num = int(input("Enter a number: "))
result = testfact.factorial(num)
print("Thee factorial of",num,"is",result)'''

# factorial_module.py

def factorial(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial(x - 1)

# main_program.py

import factorial_module

def main():
    num = int(input("Enter a number: "))
    result = factorial_module.factorial(num)
    print("The factorial of", num, "is", result)

if __name__ == "__main__":
    main()
