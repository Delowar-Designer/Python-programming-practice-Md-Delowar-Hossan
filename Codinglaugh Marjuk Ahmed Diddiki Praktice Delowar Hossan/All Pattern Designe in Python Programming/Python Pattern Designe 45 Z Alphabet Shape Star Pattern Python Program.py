# Python Pattern Designe 45 Z Alphabet Shape Star Pattern Python Program
i = 1
j = 3
x = input("Enter Pattern Print View value: ")

for row in range(0,5):
    for col in range(0,5):
        if(row==0 or row==4):
            print(x," ",end="")
        elif(row==i and col==j):
            print(x," ",end="")
            i = i+1
            j = j-1
        else:
            print("   ",end="")
    print()