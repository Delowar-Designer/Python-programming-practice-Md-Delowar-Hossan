# Python Pattern Designe 5 Invrted Mirrored Right Triangle
a = int(input("Enter a value: "))

for i in range(a,0,-1):
    s = i-1
    for j in range(0,i):
        print("#",end="")
    print()
    for k in range(0,a-s):
        print(" ",end="")