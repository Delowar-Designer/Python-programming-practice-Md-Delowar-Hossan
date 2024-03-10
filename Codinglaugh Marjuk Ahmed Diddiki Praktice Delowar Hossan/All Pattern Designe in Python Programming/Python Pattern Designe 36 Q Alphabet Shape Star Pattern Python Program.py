# Python Pattern Designe 36 Q Alphabet Shape Star Pattern Python Program
x = input("Enter Pattern Print View value: ")

for row in range(0,7):
    for col in range(0,7):
        if(((row==0 or row==5) and (col>0 and col<4)) or ((col==0) and (row>0 and row<5))or(col==4 and (row!=0 and row!=5 and row!=7))or(row==7 and col==5)):
            print(x," ",end="")
        else:
            print("   ",end="")
    print()