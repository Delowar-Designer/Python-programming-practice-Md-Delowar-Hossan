# Python Pattern Designe 44 Y Alphabet Shape Star Pattern Python Program
i = 0
j = 6
x = input("Enter Pattern Print View value: ")

for row in range(0,7):
    for col in range(0,7):
        if((row==col and col<3)or(col==3 and (row>2 and row<7))):
            print(x," ",end="")
        elif(row==i and col==j):
            print(x," ",end="")
            i = i+1
            j = j-1
        else:
            print("   ",end="")
    print()