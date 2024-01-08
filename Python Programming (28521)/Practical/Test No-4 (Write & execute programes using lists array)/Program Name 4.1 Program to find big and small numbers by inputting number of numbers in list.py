# Program to find big and small numbers by inputting number of numbers in list
NumList = []
Number = int(input("Please enter the Toral Number of List Elements: "))
for i in range(1, Number +1):
    value = int(input("Please enter the Value of %d Element: "%i))
    NumList.append(value)

print("\nThe Smallest Element in this List is: ",min(NumList))
print("The Largest Element in this List is : ",max(NumList))
