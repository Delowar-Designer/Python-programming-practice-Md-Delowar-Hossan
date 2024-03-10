# Python Pattern Designe 51 Hollow Diamond Pattern Python Program
#y = int(input("Enter Area Size value of Number: "))
x = input("Enter Pattern Print View value Boder: ")

for row in range(0,9):
    for col in range(0,9):
        if (row+col==4 or col-row==4 or row-col==4 or row+col==12):
            print(x,"",end="")
        else:
            print(" ",end="")
    print()