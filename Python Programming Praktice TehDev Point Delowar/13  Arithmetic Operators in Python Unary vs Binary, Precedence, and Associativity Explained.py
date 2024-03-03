#  Arithmetic Operators in Python: Unary vs Binary, Precedence, and Associativity Explained
x = 12
y = 5

z = x + y
print(z)
z = x - y
print(z)
z = x * y
print(z)
z = x / y
print(z)
z = x ** y
print(z)
z = x % y
print(z)
z = x // y
print(z)
t = x + y * x
print(t)

h = 10 * 2 / 2 # 10
# 20
# 20/2
# 10
print(h)

k = 2 + 3 * 4 ** 2 - 1 # 49
# 4** 2 = 16
# 3 * 16 = 48
# 2 + 48 = 50
# 50 - 1 = 49
print(k)

g = (2 + 3) * 4** 2 - 1 #79
# 2 + 3 = 5
# 4 ** 2 = 16
# 5 * 16 = 80
# 80 - 1 = 79
print(g)