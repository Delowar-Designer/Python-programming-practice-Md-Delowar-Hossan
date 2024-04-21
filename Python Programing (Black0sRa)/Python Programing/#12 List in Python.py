# List in Python
animal_list = ['dog', 'cat', 'rabbit', 'cow', 'panda', 'mouse']
print(animal_list[0:4])
animal_list.append("lion")
print(animal_list)
animal_list[1] = 'Zribe'
print(animal_list)
animal_list.insert(2,'rat')
print(animal_list)
animal_list.remove('dog')
print(animal_list)
del animal_list[1]
print(animal_list)
animal_list.pop()
print(animal_list)
new_list = animal_list.copy()
print(new_list)
for list in animal_list:
    print(list)
animal_list.clear()
print(animal_list)

number_list = [1,2,3,4,5,6,7,8,9]
number_list.append(4)
print(number_list)

number_list = [1,2,3,4,5,6,7,8,9]
number_list[2]=10
print(number_list)

number_list = [1,2,3,4,"name",5,6,7,8,9,"fruits"]
number_list.append(4)
print(number_list)

number_list = [1,2,3,4]
nuw_number_list = [5,6,7,9]
print(nuw_number_list + number_list)
number = [2,66,77,88]
number_list.extend(number)
print(number_list)

num_list = [1,2,3,4,5,6,7,8,99]
print(len(num_list))
print(max(num_list))
max = num_list[0]
for num in num_list:
    if num > max:
        max = num
print(max)

num_list1 = [58,1,2,3,4,5,6,7,8]
print(num_list1.sort())
num_list1.sort()
print(num_list1)
num_list1.reverse()
print(num_list1)
num_list1.sort(reverse=False)
print(num_list1)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][2])
print(matrix[2][1]+ matrix[0][2])

number2 = [2,3,5,2,8,5]
print(number2.count(2))