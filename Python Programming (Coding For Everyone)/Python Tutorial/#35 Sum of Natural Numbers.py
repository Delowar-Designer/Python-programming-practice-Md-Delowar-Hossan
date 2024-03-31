#35 Sum of Natural Numbers
num = int(input("Please enter a number "))

if num<0:
    print("Please enter a Positive Number ")
else:
    sum = 0
    while num>0:
        sum = sum + num
        num = num - 1
    print(sum)
print(num)