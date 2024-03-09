# Python Pattern Designe 14 Invertad Mirrored Right Triangle Number Pattern
a = int(input("Enter a value: "))

for i in range(a+1,1,-1):
    print(" "*(a+1-i),end="")
    for j in range(1,i):
        print(j,end="")
    print()


b = int(input("Enter b value: "))

for i in range(b+1,1,-1):
    print(" "*(b+1-i),end="")
    for j in range(1,i):
        print(i-1,end="")
    print()