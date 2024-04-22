# Multiple inputs in one line
x, y = map(int,input().split())
print(x,y)
print(y,x)

number = list(map(int,input("Provide some numbers: ").split()))
print(*number)