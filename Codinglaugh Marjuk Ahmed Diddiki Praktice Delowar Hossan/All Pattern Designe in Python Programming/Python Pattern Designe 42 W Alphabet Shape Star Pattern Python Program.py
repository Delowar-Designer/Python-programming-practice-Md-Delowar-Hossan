# Python Pattern Designe 42 W Alphabet Shape Star Pattern Python Program
i = 0
j = 12
x = input("Enter Pattern Print View value: ")

for row in range(0,5):
    for col in range(0,13):
        if(row==col or (row==3 and (col==5 or col==7)) or (row==2 and col==6)):
            print(x,"",end="")
        elif(row==i and col==j):
            print(x,"",end="")
            i = i+1
            j = j-1
        else:
            print("  ",end="")
    print()