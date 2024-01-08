# Program to display odd numbers from 1 to N on monitor screen
# print odd number
n=int(input("Enter the end of Range = "))
print("Printing of add Numbers Series: ")
for i in range(1,n+1):
    if (i%2):
        print(i,end=", ")