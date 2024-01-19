# Write a program to shorten the elements of a list from largest to smallest
lists = []
m = int(input("How Many lnput in List= "))
for i in range(m):
    value = int(input("Enter ltem= "))
    lists.append(value)
lists.sort(reverse= True)
print("Sorting of List=",lists)


