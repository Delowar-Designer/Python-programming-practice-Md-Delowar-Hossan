# Python Pattern Designe 6 Star Pattern
a = int(input("Enter a value: "))

for i in range(1, a + 1):
    for k in range(0,a - i):
        print(" ",end="")
    for j in range(1, i + 1):
        print("@ ",end="")
    print()