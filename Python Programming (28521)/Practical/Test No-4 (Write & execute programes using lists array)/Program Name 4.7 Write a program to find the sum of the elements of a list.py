# Write a program to find the sum of the elements of a list
items = []
n = int(input("How Many Input in List= "))
for i in range(n):
    value = input("Enter Item= ")
    items.append(value)
sum = 0
for i in items:
    sum = sum + int(i)
print("Summation of List= ",sum)


