# Python Pattern Designe 37 R Alphabet Shape Star Pattern Python Program
x = input("Enter Pattern Print View value: ")

for row in range(0,7):
    for col in range(0,5):
        if(col==0 or (col==4 and (row==1 or row==2 or row==6)) or ((row==0 or row==3) and (col>0 and col<4)) or (row==4 and col==2)or (row==5 and col==3)):
            print(x," ",end="")
        else:
            print("   ",end="")
    print()