# Set in Python
number = [1,2,3,2,3,4,5,6,7,2,3,4]
unique_number = []
for num in number:
    if num not in unique_number:
        unique_number.append(num)
    else:
        continue
print(unique_number)
print(set(unique_number))

number = {1,2,3,2,3,4,5,6,7,2,3}
print(number)
number.update([])
