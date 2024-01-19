# Program Name 4.4 Print all index number of the same item
items =[]
n = int(input("How Many Input in List = "))
for i in range(n):
    value = input("Enter Item= ")
    items.append(value)

for index, item in enumerate(items):
    print(index, item)

# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
rditems = Remove(items)
for i in rditems:
    get_index = []
    item = i
    loc = 0
    for j in items:
        if(item==j):
            get_index.append(loc)
        loc=loc+1
    print(item,"index Value = ",get_index)
    

