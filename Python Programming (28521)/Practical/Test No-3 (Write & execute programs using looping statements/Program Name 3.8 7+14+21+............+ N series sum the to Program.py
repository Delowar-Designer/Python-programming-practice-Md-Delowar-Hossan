# 7+14+21+............+ N series sum the to Program
n = int(input("Enter the end of range, N = "))
sum = 0
for i in range(7,n+1,7):
    sum = sum + i
print("7+14+21+.........+",n,"=",sum)
