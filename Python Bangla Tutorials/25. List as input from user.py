# List as input from user
n = input("Enter a text of number: ")

list = n.split()
sum = 0

for number in list:
    sum = sum + int(number)
print("The sum of", sum)
