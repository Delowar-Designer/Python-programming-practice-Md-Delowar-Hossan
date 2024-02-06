# Program to find product of numbers using functions
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((8,2,3,10,7)))

