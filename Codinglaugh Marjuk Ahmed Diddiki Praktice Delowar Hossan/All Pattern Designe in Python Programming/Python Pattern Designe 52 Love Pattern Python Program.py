# Python Pattern Designe 52 Love Pattern Python Progrram
x = input("Enter Pattern Print View value Boder: ")
for row in range(0,6):
    for col in range(0,7):
        if((row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8)):
            print(x," ",end="")
        else:
            print("   ",end="")
    print()
