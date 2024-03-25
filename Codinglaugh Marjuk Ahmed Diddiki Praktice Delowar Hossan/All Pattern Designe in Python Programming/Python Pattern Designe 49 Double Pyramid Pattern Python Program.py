# Python Pattern Designe 49 Double Pyramid Pattern Python Program
a = int(input("Enter Area Size value of Number: "))
x = input("Enter Pattern Print View value Boder: ")

for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(x,"",end="")
    print(" "*((a-i)*2),end="")
    for k in range(1,i+1):
        print(x,"",end="")
    print()

for i in range(1,a+1):
    print(" "*(a-i)+"* "*i+" "*((a-i)*2)+"* "*i)