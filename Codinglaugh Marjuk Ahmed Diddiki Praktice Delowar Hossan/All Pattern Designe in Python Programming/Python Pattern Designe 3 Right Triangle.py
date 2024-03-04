# Python Pattern Designe 2 Right Triangle
a = int(input("Enter a value: "))

for i in range(1,a+1):
    if i%2 != 0:
        for t in range(1, i + 1):
            print("* ", end="")
        print()
for l in range(1,a+1):
    k = l
    for y in range(1, l + k):
        print("D ", end="")
        k = 2
    print()
