# Python Pattern Designe 26 G Alphabet Shape Star Pattern Python Program
x = input("Enter Pattern Print View value: ")

for row in range(0,7):
    for col in range(0,6):
        if(((col==0) and (row!=0 and row!=6)) or ((col==4)and (row!=1 and row!=2 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)) or ((row==3) and (col==3 or col==5))):
            print(x," ",end="")
        else:
            print("  ",end="")
    print()