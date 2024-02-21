#42 Python Join Sets
# the union() methid returns a new set with all items from both sets:
set1 = {"a","b","c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set2.update(set1)
print('Update',set2)