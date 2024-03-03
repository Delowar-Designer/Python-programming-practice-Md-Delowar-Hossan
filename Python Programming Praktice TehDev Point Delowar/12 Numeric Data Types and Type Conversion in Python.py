# Numeric Data Types and Type Conversion in Python
# integer
num_int = float(32)
print(num_int)
print(type(num_int))

# float
num_float = int(3.14)
print(num_float)
print(type(num_float))
num_float1 = int(1e10) # 1x10^-3
print(num_float1)
print(type(num_float1))

# complex
num_complex = 2 + 4j
print(num_complex)
print(type(num_complex))
print(num_complex.real)
print(num_complex.imag)
print(float(num_complex.imag))
num_complex = complex(2)
print(num_complex)
print(type(num_complex))