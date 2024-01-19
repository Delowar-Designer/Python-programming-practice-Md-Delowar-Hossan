# Write a program to shorten the elements of a list from smallest to largest
list = []
n = int(input("How Many Input in List= "))
for i in range(n):
    value = int(input("Enter Value Item= "))
    list.append(value)
list.sort()
print("Sorting of List= ",list)