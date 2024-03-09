# Python Pattern Designe 14 Pyramid star pattern program
a = int(input("Enter a value: "))
k = 1
for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,k+1):
        print("*",end="")
    print()
    k = k+2

b = int(input("Enter b value: "))
d = 1
for i in range(1,b+1):
    print(" "*(b-i)+"*"*d)
    d = d+2

