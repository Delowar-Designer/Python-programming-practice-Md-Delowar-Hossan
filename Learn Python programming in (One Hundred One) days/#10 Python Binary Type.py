#10 Python Binary Type
# Binary Types:	bytes, bytearray, memoryview
number = [1,2,3,4,5,6,7,8,9,121,255]
b = bytes(number)

print(type(b))
print(type(number))

# Binary type data byteArray
number1 = [1,2,3,4,5,6,7,8,9,121,255]
b1 = bytearray(number1)
b1[2] = 100

print(type(b1))
print(type(number1))
print(b1[2])
print(b1[1])
print(number1)


