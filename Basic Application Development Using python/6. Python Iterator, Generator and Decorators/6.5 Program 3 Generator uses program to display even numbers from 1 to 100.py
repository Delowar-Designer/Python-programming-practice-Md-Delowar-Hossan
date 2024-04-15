# Generator uses program to display even numbers from 1 to 100
# creating a funcction that accepts a number as an argument
def evenNumbers(num):
    for i in range(1,num+1):
        if (i%2!=1):
            yield i
result = evenNumbers(100)
for i in result:
    print(i,end=" ")
