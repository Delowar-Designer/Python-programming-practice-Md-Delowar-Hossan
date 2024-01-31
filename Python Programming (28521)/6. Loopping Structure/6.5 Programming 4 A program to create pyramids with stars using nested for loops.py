# A program to create pyramids with stars using nested for loops
h = int(input("Enter the height of the piramid: "))
for row in range (1,h+1):
    # Loop to print the space
    for cal in range(1,h-row+1):
        print(" ",end="")
    # Loop to print *
    for col in range(0,2*row-1):
        print("*",end="")
    # to print a new line
    print()
