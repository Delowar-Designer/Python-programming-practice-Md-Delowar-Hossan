# Python Pattern Designe 24 D Alphabet Shape Star Pattern Python Program
x = input("Enter Pattern Print View value: ")

for row in range(0,7):
    for col in range(0,5):
        if((col==0) or ((row==0 or row ==3 or row==6)and (col>0 and col<5))):
            print(x," ",end="")
        else:
            print("  ",end="")
    print()