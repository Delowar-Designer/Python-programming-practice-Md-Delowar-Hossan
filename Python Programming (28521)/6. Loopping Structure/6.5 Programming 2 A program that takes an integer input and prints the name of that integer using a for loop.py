# A program that takes an integer input and prints the name of that integer using a for loop
flag = 0
number = int(input("Enter the number: "))
for x in range(2,number):
    if(number % x == 0):
        flag = True
        break
if flag:
    print(number,"is not a prime number.")
else:
    print(number,"is aprime number.")
