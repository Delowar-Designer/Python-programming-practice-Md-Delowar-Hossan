# Factorial of a Number
num = int(input("Enter your number: "))
result = 1

for i in range(num,0,-1):
    result = result * i
print(f"Factorial of {num} is {result}")
