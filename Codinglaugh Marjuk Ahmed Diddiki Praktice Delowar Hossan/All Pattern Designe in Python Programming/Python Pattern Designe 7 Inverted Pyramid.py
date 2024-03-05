# Python Pattern Designe 7 Inverted Pyramid
x = int(input("Enter a value: "))
a = input("Enter Pattern Print View value: ")

for i in range(x, 0, -1):
    for k in range(0, x - i):
        print(" ", end="")
    for j in range(0, i):
        print(a, "", end="")
    print()
