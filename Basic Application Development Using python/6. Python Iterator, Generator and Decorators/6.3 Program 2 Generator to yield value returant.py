# Generator to yield value returant
# creating a function that accepts a number as an argument
def oddNumbers(num):
    # traversing till that number passed
    for i in range(num):
        # Cheking whether the iterator indax value is an odd number
        if (i%2!=0):
            # getting the iterator index value if the condition is true using the yield keyword
            yield i
# calling the above funtion to get the odd numbers below 8
result = oddNumbers(8)
# calling the next items in the result list
print(next(result))
print(next(result))
print(next(result))
print(next(result))
# throws an error since the list has on more elemenths
print(next(result))