# Python Pattern Designe 17 Diamond Number Pattern Python Program
a = int(input("Enput a value: "))

for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()

for i in range((a-1),0,-1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()


for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range((a-1),0,-1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()