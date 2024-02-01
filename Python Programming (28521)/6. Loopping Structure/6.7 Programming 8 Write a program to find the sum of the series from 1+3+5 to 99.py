# Write a program to find the sum of the series from 1+3+5 to 99
print("Enter the range of number:")
n = int(input())
sum = 0
i = 1
while (i <= n):
    sum += i;
    i += 2
print("The sum off the series =",sum)
