# Python Pattern Designe 48 Hollow Pattern Python Program
#y = int(input("Enter Area Size value of Number: "))
x = input("Enter Pattern Print View value Boder: ")
#z = input("Enter Pattern Print View a value Inside: ")

for row in range(0,5):
    for col in range(0,9):
        if(row+col==4 or ((col-row==4)and row!=0)):
            print(x,"",end="")
        else:
            print("  ",end="")
    print()

for row in range(0,5):
    for col in range(0,9):
        if(row+col==4 or ((col-row==4)and row!=0)):
            print(row+1,end="")
        else:
            print("  ",end="")
    print()
