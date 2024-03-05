# Python Pattern Designe 8 Diamind star pattern
x = int(input("Enter a value: "))
a = input("Enter Pattern Print View value: ")

for i in range(0,x):
    print(" "*(x-i-1)+(a+' ')*(i+1))

for j in range(x-1,0,-1):
    print(" "*(x-j)+(a+' ')*(j))

