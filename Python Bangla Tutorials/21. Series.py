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

# 1^2 + 2^2 + 3^2 + … + n^2
n = int(input("Enter the Last number Square : "))
sum0 = 0

for x in range(1, n+1, 1):
    sum0 = sum0 + x * x
print("The sum of Square : ", sum0)

# 2^2 + 4^2 + 6^2 + … + n^2
n = int(input("Enter the Square Last even number : "))
sum6 = 0

for x in range(2, n+1, 2):
    sum6 = sum6 + x * x
print("sum of even numbers Square : ", sum6)

# 1 + ½ + 1/3 + …. + 1/n
n = int(input("Enter the value of n: "))
sum7 = 0

for x in range(1, n + 1):
    sum7 = sum7 + 1 / x

print("Sum of the harmonic series:", sum7)

# 2 x 4 x 6 x …. x n  (sum of even numbers from 1-n )
n = int(input("Enter the Multipication Last even number : "))
sum5 = 1

for x in range(2, n+1, 2):
    sum5 = sum5 * x
print("sum of even numbers Multipication : ", sum5)

# 1 x 3 x 5 x …. x n  (sum of odd numbers from 1-n )
n = int(input("Enter the Multipication Last odd number : "))
sum4 = 1

for x in range(1, n+1, 2):
    sum4 = sum4 * x
print("sum of odd numbers Multipication : ", sum4)

# 4 x 8 x 12 x … x n
n = int(input("Enter the Multipication Last even 4 number : "))
sum3 = 1

for x in range(4, n+1, 4):
    sum3 = sum3 * x
print("sum of even 4 numbers Multipication : ", sum3)

# 1^2 x 2^2 x 3^2 x … x n^2
n = int(input("Enter the Multipication Last number Square : "))
sum8 = 1

for x in range(1, n+1, 1):
    sum8 = sum8 * x * x
print("The Multipication of Square : ", sum8)

# 2^2 x 4^2 x 6^2 x ..... x n^2
n = int(input("Enter the Multipication Last even 2 number : "))
sum9 = 1

for x in range(2, n+1, 2):
    sum9 = sum9 * x * x
print("The Multipication of square 2 : ", sum9)
