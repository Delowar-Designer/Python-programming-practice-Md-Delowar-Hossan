'''marks = 10000
a = marks / 0
print(a)'''

'''x = -1
if x < 0:
    raise Exception("Sorry, on numbers below zero")
'''
'''x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
'''
'''a = 5
b = 5
try:
    # candition for checking for negative values
    if a < 0 or b < 0:
        # raising exception using keyword
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("Please enter valid integer value")'''

def square(x):
    assert x>=0, 'Only positive numbers are allowed'
    return x*x
try:
    square(-2)
except AssertionError as msg:
    print(msg)
