# Python Pattern Designe 11 Pyramid__ Number pattern
a = int(input("Enter the value: "))

for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(j," ",end='')
    print()

for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(i," ",end='')
    print()