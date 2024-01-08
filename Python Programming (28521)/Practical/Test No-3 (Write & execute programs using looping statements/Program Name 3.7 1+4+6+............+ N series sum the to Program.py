# 2+4+6+............+ N series sum the to Program
n = int(input("Enter the end of range = "))
sum = 0
for i in range(2,n+1,2):
    sum = sum + i
print("2+4+6+.......+",n,"=",sum)
