# 1+3+5+............+ N series sum the to Program
n = int(input("Enter the end of range = "))
sum = 0
for i in range(1,n+1,2):
    sum = sum + i
print("1+3+5+............+",n,"=",sum)