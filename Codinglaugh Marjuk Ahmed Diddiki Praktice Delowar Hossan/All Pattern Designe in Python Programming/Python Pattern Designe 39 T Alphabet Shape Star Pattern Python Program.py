# Python Pattern Designe 39 T Alphabet Shape Star Pattern Python Program
x = input("Enter Pattern Print View value: ")

for row in range(0,6):
    for col in range(0,5):
        if (row==0 or (col==2 and (row>0 and row<6))):
            print(x," ",end="")
        else:
            print("   ",end="")
    print()