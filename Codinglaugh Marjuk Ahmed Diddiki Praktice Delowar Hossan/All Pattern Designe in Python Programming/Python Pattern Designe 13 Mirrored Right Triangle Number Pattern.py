# Python Pattern Designe 13 Mirrored Right Triangle Number Pattern
a = int(input("Enter a value: "))

for i in range(0,a):
    print(" "*(a-i-1),end="")
    for j in range(0,i+1):
        print(j+1,end="")
    print()

b = int(input("Enter a valur2: "))
for i in range(0,b):
    print(" "*(b-i-1),end="")
    for j in range(0,i+1):
        print(i+1,end="")
    print()