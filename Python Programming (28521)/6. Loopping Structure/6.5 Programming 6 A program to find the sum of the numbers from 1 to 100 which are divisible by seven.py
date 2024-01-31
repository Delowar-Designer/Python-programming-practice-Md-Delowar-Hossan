# A program to find the sum of the numbers from 1 to 100 which are divisible by seven
n = 1
sum = 0
while n <= 100:
    if n % 7 == 0:
        sum = sum + n
    n = n + 1
print("The sum of the series = ",sum)