# ৪- ফাংশন ব্যবহার করে কোন সংখ্যার মৌলিক কি না তা নির্ণয়ের  প্রোগ্রাম।
# 4- Program to determine whether a number is prime or not using functions.
def test_prime(n):
    if(n==1):
        return False
    elif(n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
print(test_prime(int(input("input number:"))))

'''

def test_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


# Taking input from the user
number = int(input("Input number:"))

# Calling the function and printing the result
result = test_prime(number)
print(f"{number} is prime: {result}")
'''
