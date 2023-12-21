# Recursion Example
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

numbers = int(input("Enter a fact number: "))
print(fact(numbers))
