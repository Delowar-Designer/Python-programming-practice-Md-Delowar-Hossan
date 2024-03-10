# Python Pattern Designe 46 input Shape Star Pattern Python Program
x = input("Enter Pattern Print View value: ")
y = int(input("Enter area size value: "))

for row in range(0,y):
    for col in range(0,y):
        if(col==0 or col==(y-1) or ((row==0 or row==(y-1)) and (col>0 and col<(y-1)))):
            print(x," ",end="")
        else:
            print("   ",end="")
    print()