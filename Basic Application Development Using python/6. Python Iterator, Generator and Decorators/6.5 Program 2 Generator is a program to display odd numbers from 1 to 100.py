# Generator is a program to display odd numbers from 1 to 100
# creating a function that accepts a number as an argument
def odd_numbers(num):
    # traversing till that number passed
    for i in range(num):
        # checking whether the iterator index value is an odd number
        if(i%2!=0):
            # getting the iterator index value if the condition is true using the yield keyword
            yield i
# callijng the above function to get the odd numbers below  8
result = odd_numbers(100)
# calling the next items in the result list
for i in result:
    print(i,end=" ")
