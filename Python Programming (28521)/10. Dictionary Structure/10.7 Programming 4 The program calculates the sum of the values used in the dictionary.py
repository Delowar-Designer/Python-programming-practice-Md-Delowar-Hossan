# The program calculates the sum of the values used in the dictionary
dict = {'a':100,'b':200,'c':500}
sum = 0
for i in dict:
    sum = sum + dict[i]
print("The summation of the dictionary is: ",sum)
