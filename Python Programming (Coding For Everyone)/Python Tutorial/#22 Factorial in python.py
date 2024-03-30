# Factorial in Python
def fact(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res

result=fact(4)
print(result)