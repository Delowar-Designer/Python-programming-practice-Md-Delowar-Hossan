#4 Identity Membership, Logical Operators in Python
a = 2
b = 10
print(a>1 and b<12)
print(a>3 or b<8)
print(not(a>3))

# Identity operators
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = list_1
print(list_1 is not list_3)

# Membership operators
list_1 = [1, 2, 3]
print(2 in list_1)
print(2 not in list_1)