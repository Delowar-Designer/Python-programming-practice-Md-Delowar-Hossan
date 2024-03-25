# Python Pattern Designe 19 Mirrored Half Diamond Pattern Python Program
a = int(input("Enter a value: "))

for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range((a-1),0,-1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(1,a+1):
    print(" "*(a-i)+"*"*i)

for i in range((a-1),0,-1):
    print(" "*(a-i)+"*"*i)