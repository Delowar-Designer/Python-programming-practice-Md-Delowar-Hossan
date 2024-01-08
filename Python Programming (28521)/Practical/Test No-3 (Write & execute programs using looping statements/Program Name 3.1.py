# Program to display even numbers from one to n on monitor screen
# Print even Number
n = int(input("Enter the end of Range = "))
print("Printing of Even Number Series: ")
for i in range(1,n+1):
    if not(i%2):
        print(i,end=", ")
