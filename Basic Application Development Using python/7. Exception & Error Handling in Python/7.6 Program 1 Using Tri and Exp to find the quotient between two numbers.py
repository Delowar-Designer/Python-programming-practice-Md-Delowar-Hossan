# Using Tri and Exp to find the quotient between two numbers
a = 10
b = 9
try:
    # condition for checking for negative values
    if a < 0 or b < 0:
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("Please enter valid integer value")

