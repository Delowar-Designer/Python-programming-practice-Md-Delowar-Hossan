# Returning Value From Funciton
def add (a,b):
    sum = a + b
    return sum
result = add(20,30)
print("Result = ",result)


def large(a,b):
    if a>b:
        return a
    else:
        return b
result = large(20,25)
print("Result = ",result)

print(large(55,100))
maximum = large
print("maximum = ",maximum(47,48))