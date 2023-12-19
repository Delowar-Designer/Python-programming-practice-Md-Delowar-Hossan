# Series
# 1 + 2 + 3 ....+n
n = int(input("Enter the Last number : "))
sum = 0

for x in range(1,n+1,1):
    sum = sum + x
print("The sum of", sum)


# 2 + 4 + 6 + ....+ n (sum of even numbers from1-n
n = int(input("Enter the Last even number : "))
sum = 0

for x in range(2,n+1,2):
    sum = sum + x
print("sum of even numbers : ", sum)

# 1 + 3 + 5....+n(sum of odd number from 1-n)
n = int(input("Enter the Last odd number : "))
sum1 = 0

for x in range(1, n+1, 2):
    sum1 = sum1 + x
print("sum of odd numbers : ", sum1)

# 4 + 8 + 12 + … + n
n = int(input("Enter the Last even 4 number : "))
sum2 = 0

for x in range(4, n+1, 4):
    sum2 = sum2 + x
print("sum of even 4 numbers : ", sum2)

# 5) 1^2 + 2^2 + 3^2 + … + n^2
# 6) 2^2 + 4^2 + 6^2 + … + n^2
# 7) 1 + ½ + 1/3 + …. + 1/n
# 8) 2 x 4 x 6 x …. x n  (sum of even numbers from 1-n )
# 9) 1 x 3 x 5 x …. x n  (sum of odd numbers from 1-n )
# 10) 4 x 8 x 12 x … x n
# 11) 1^2 x 2^2 x 3^2 x … x n^2
# 12) 2^2 x 4^2  x 6^2 x … x n^2