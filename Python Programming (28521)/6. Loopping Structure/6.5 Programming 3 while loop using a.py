# while loop using a 1*2+2*2+3*2+................+N*2=
N = int(input("Enter the value of N: "))
sum = 0;
i = 1
while i <= N:
    sum = sum + i*i
    i = i + 2
print("The sum of the series is: ",sum)
