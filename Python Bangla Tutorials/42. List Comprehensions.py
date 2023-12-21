# List Comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [expression for item in list]
result = [x*x for x in numbers]
print(result)

result = list(map(lambda x : x*x,numbers))
print(result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(filter(lambda x : x%2 == 0, numbers))
print(result)

result = [x for x in numbers if x%2==0]
print(result)