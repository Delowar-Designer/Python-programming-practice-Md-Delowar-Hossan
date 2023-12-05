#৩- ফাংশন ব্যবহার করে কতগুলো সংখ্যার গুনফল নির্ণয়ের  প্রোগ্রাম।
#3- Program to calculate product of numbers using functions.
def multoply(numbers):
    total=1
    for x in numbers:
        total *= x
    return total
print(multoply((8,2,3,10,7)))
