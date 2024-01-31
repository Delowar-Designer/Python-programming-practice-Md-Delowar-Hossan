# Python Fibonacci Series Calculation Program Using While Loops
f1 = 0
f2 = 1
fibo = 1
i = 2
n = int(input("Enter n: "))
print(f1,f2,end=" ")
while (i < n):
    fibo = f1 + f2
    f1 = f2
    f2 = fibo
    print(fibo,end=" ")
    i = i + 1

