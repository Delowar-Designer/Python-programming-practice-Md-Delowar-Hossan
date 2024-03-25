# Python Pattern Designe 48 Hollow Rriangle Pattern Python Program
y = int(input("Enter Area Size value of Number: "))
x = input("Enter Pattern Print View value Boder: ")
#z = input("Enter Pattern Print View a value Inside: ")

for row in range(0,y):
    for col in range(0,y):
        if(col==0 or (row==(y-1)and(col>0 and col<y))or((row==col)and(col!=0 and col!=(y-1)))):
            print(x,"",end="")
        else:
            print("  ",end="")
    print()
