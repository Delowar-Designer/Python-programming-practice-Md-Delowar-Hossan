# List is a program to find large numbers and locations by inputting a number of numbers
NumList = []
Number = int(input("Please enter the Number of List Elements: "))
for i in range(1,Number + 1):
    value = int(input("Please enter the Value of %d Element: "%i))
    NumList.append(value)
i=1
max = NumList[0]
while(i<Number):
    if(max<NumList[i]):
        max = NumList[i]
        loc = i
    i = i + 1
print("The largest Element in this List is:", max,"and Location = ",loc +1)
