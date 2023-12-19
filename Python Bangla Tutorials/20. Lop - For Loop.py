# Lop - For Loop
num = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(num)

index = 0
while index<9 :
    print(num[index])
    index = index + 1
    
    
num = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(num)

index = 0
n = len(num)
while index<n :
    print(num[index])
    index = index + 1

num = [10, 20, 30, 40, 50, 60, 70, 80]
for x in num:
    print(x)

num = [10, 20, 30, 40, 50, 60, 70]
sum = 0
for x in num:
    sum = sum + x
print("sum : ",sum)