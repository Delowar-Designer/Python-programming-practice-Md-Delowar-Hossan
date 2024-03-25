# Python Pattern Designe 47 input Shape Number Pattern Python Program
y = int(input("Enter Area Size value of Number: "))
x = input("Enter Pattern Print View value Boder: ")
z = input("Enter Pattern Print View a value Inside: ")

for row in range(0,y):
    for col in range(0,y):
        if(col==0 or col==(y-1) or ((row==0 or row==(y-1)) and (col>0 and col<(y-1)))):
            print(x," ",end="")
        else:
            print(z," ",end="")
    print()


'''for row in range(0,5):
    for col in range(0,5):
        if(col==0 or col==4 or ((row==0 or row==4) and (col>0 and col<4))):
            print(x,"",end="")
        else:
            print("0 ",end="")
    print()'''