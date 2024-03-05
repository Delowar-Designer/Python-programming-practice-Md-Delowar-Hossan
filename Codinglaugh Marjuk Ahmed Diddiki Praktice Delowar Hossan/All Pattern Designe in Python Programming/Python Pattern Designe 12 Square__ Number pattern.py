# Python Pattern Designe 12 Square__ Number pattern
a = int(input("Enter the value: "))

for i in range(1,a+1):
    for j in range(1,a+1):
        print(i,end="")
    print()

b = input("Enter the Your Value: ")

for i in range(1,a+1):
    for j in range(1,a+1):
        if(i == j):
            print(b,end="")
        else:
            print(i,end="")
    print()