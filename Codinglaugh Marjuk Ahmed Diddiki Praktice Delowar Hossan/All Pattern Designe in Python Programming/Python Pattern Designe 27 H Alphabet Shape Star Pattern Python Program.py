#  Python Pattern Designe 27 H Alphabet Shape Star Pattern Python Program
x = input("Enter Pattern Print View value: ")

for row in range(0,7):
    for col in range(0,5):
        if(col==0 or col==4 or ((row==3 and (col>0 and col<4)))):
            print(x," ",end="")
        else:
            print("   ",end="")
    print()