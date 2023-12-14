# craete a set
integer_set = {1, 2, 3}
print(integer_set)
mixed_set = {1, 2, 3, "Hello"}
print(mixed_set)

# craete empty a set
set1 = {}
print(type(set1))
set2 = set()
print(type(set2))
months = {"january", "february", "march"}
print(months)
# add method
months.add("april")
print(months)
months.update(["may", "june", "july"])
print(months)
# remove items
months.discard("february")
print(months)
