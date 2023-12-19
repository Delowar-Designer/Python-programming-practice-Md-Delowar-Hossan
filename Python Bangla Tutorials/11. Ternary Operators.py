# Ternary Operators
num1 = 90
num2 = 50
if num1 > num2:
    print("num1 > num2:", num1)
else:
    print("num2 > num1:", num2)

num3 = 41
num4 = 45
print(num1 if num1 > num2 else num2)
max = num1 if num2 > num3 else num3
print("Maximum", max)
