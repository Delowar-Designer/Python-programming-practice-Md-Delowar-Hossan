# Program to determine whether a number is prime or not using functions
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n% x==0):
                return False
            return True
print(test_prime(int(input("Input number:"))))
