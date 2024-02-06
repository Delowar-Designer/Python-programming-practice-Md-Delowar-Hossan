# Program to find the factorial value of a number using functions
def factroial(n):
    if n == 0:
        return 1
    else:
        return n * factroial(n-1)
n = int(input("Input a number to compute the factorial: "))
print(factroial(n))