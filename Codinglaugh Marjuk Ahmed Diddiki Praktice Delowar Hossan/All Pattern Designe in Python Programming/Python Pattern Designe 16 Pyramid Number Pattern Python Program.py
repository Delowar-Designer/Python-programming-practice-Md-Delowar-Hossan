# Python Pattern Designe 16 Pyramid Number Pattern Python Program
#a = int(input("Enter a value: "))
k = 1
'''for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,k+1):
        print(i,end="")
    print()
    k = k+2'''

b = int(input("Enter b value: "))
p = 1
for i in range(1,b+1):
    print(" "*(b-i),end="")
    for j in range(1,k+1):
        print(p,end="")
    print()
    k = k+2
    p = p+2
