# Write a Program to find Fivonacci series in python using Function
def fib():
    n = int(input("Enter how many terms: "))
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib()
