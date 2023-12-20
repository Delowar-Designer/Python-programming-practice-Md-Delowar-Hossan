# Series Prigrame All 1 intput
n = int(input("Enter the Last number : "))
# 1 + 2 + 3 ....+n
print("1 + 2 + 3 ....+n")
print("Enter the Last number : ")
sum = 0

for x in range(1,n+1,1):
    sum = sum + x
print("The sum of", sum)

# 2 + 4 + 6 + ....+ n (sum of even numbers from1-n
print("2 + 4 + 6 + ....+ n (sum of even numbers from1-n")
print("Enter the Last even number : ")
sum = 0

for x in range(2,n+1,2):
    sum = sum + x
print("sum of even numbers : ", sum)

# 1 + 3 + 5....+n(sum of odd number from 1-n)
print("1 + 3 + 5....+n(sum of odd number from 1-n)")
print("Enter the Last odd number : ")
sum = 0

for x in range(1, n+1, 2):
    sum = sum + x
print("sum of odd numbers : ", sum)

# 4 + 8 + 12 + … + n
print("4 + 8 + 12 + … + n")
print("Enter the Last even 4 number : ")
sum = 0

for x in range(4, n+1, 4):
    sum = sum + x
print("sum of even 4 numbers : ", sum)

# 1^2 + 2^2 + 3^2 + … + n^2
print("1^2 + 2^2 + 3^2 + … + n^2")
print("Enter the Last number Square : ")
sum = 0

for x in range(1, n+1, 1):
    sum = sum + x * x
print("The sum of Square : ", sum)

# 2^2 + 4^2 + 6^2 + … + n^2
print("2^2 + 4^2 + 6^2 + … + n^2")
print("Enter the Square Last even number : ")
sum = 0

for x in range(2, n+1, 2):
    sum = sum + x * x
print("sum of even numbers Square : ", sum)

# 1 + ½ + 1/3 + …. + 1/n
print("1 + ½ + 1/3 + …. + 1/n")
print("Enter the value of n: ")
sum = 0

for x in range(1, n + 1):
    sum = sum + 1 / x

print("Sum of the harmonic series:", sum)

# 2 x 4 x 6 x …. x n  (sum of even numbers from 1-n )
print("2 x 4 x 6 x …. x n  (sum of even numbers from 1-n )")
print("Enter the Multipication Last even number : ")
sum = 1

for x in range(2, n+1, 2):
    sum = sum * x
print("sum of even numbers Multipication : ", sum)

# 1 x 3 x 5 x …. x n  (sum of odd numberprint)
print("1 x 3 x 5 x …. x n  (sum of odd numberprint)")
print("Enter the Multipication Last odd number : ")
sum = 1

for x in range(1, n+1, 2):
    sum = sum * x
print("sum of odd numbers Multipication : ", sum)

# 4 x 8 x 12 x … x n
print("4 x 8 x 12 x … x n")
print("Enter the Multipication Last even 4 number : ")
sum = 1

for x in range(4, n+1, 4):
    sum = sum * x
print("sum of even 4 numbers Multipication : ", sum)

# 1^2 x 2^2 x 3^2 x … x n^2
print("1^2 x 2^2 x 3^2 x … x n^2")
print("Enter the Multipication Last number Square : ")
sum = 1

for x in range(1, n+1, 1):
    sum = sum * x * x
print("The Multipication of Square : ", sum)

# 2^2 x 4^2 x 6^2 x ..... x n^2
print("2^2 x 4^2 x 6^2 x ..... x n^2")
print("Enter the Multipication Last even 2 number : ")
sum = 1

for x in range(2, n+1, 2):
    sum = sum * x * x
print("The Multipication of square 2 : ", sum)

