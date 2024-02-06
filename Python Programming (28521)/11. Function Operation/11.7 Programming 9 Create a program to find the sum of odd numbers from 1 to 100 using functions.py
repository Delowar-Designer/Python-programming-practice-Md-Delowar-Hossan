# Create a program to find the sum of odd numbers from 1 to 100 using functions
def summation():
    n = 1
    sum = 0
    for i in range(1,101):
        if n%2 == 0:
            continue
        sum = sum + n
    return sum
add = summation()
print("The summation is:",add)


def sum_of_odd_numbers():
    total_sum = 0
    for num in range(1, 101):
        if num % 2 != 0:  # Checking if the number is odd
            total_sum += num  # Adding the odd number to the total sum
    return total_sum

# ফাংশনটি কল করে বিজোড় সংখ্যাগুলোর যোগফল নির্ণয় করুন
result = sum_of_odd_numbers()

# ফলাফল মুদ্রণ করুন
print("বিজোড় সংখ্যাগুলোর যোগফল:", result)
