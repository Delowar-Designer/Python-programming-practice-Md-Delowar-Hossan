# 10- Program to find Fibonacci series using functions.
# ১০- ফাংশন ব্যবহার করে ফিবোনাকি সিরিজ বের করার প্রোগ্রাম।


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


n = 10
print("Fibo Series...:")
for i in range(n):
    print(fibo(i), end=" ")
