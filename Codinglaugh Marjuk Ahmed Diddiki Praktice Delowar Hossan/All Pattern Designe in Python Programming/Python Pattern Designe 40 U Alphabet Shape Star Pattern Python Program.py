# Python Pattern Designe 40 U Alphabet Shape Star Pattern Python Program
x = input("Enter Pattern Print View value: ")

for row in range(0,6):
    for col in range(0,5):
        if (((col==0 or col==4) and (row>=0 and row<5))or(row==5 and (col>0 and col<4))):
            print(x," ",end="")
        else:
            print("   ",end="")
    print()