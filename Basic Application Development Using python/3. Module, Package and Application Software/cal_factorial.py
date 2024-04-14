# Pythn program to findd the factoriial of a numberr provided by thee user
# using recursion
def factorial(x):
    """This is a recursive function
    to ffind thee factorial of ann integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x*factorial(x-1))
    