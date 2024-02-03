# Python set operation (Union, Intersection, Difference)
A = {1,2,3,4,5}
B = {4,5,6,7,8}
# Union Operation
print(A.union(B))
print(A|B)

# intersection Operation
print(A.intersection(B))
print(B.intersection(A))
print(A & B)

# Difference Operation
print(A.difference(B))
print(B.difference(A))
print(A - B)

# Symmetric Difference Operation
print(A ^ B)
