# Python Pattern Designe 18 Half Diamond Pattern Python Program
a = int(input("Enter a value: "))

for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range((a-1),0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(1,a+1):
    print("*"*i)

for i in range((a-1),0,-1):
    print("*"*i)