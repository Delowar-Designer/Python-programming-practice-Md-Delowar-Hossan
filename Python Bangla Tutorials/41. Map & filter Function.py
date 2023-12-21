# Map & Filter Function
def square(x):
    return x*x
num = [1,2,3,4,5,6,7,8,9]
result = list(map(square,num))
print(result)


num = [1,2,3,4,5,6,7,8,9]
filtered = list(filter(lambda x:x%2==0,num))
print(filtered)