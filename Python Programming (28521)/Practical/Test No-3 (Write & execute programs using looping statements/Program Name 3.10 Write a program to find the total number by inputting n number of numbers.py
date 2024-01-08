# Write a program to find the total number by inputting n number of numbers
n = int(input("How many integer number = "))
sum = 0
i = 0
while i<n:
    a = int(input())
    sum = sum + a
    i = i + 1
avg = sum/n
print("Summation of number = ",sum)
print("Average of number = ",avg)


