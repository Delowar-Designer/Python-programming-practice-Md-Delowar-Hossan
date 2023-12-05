# ৯- ফাংশন ব্যবহার করে ১ হতে ১০০ পর্যন্ত বিজোড় সংখ্যাগুলোর যোগফল নির্ণয়ের একটি প্রোগ্রাম।
# 9- A program to find the sum of odd numbers from 1 to 100 using functions.
def summation():
    n = 1
    sum = 0
    for n in range(100):
        if n % 2 == 0:
            continue
        sum = sum + n
    return sum


add = summation()
print("The summation is:", add)
