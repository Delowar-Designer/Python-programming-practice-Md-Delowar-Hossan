# Lamda Functopn
def calculate(a,b):
    return a*a + 2*a*b + b*b

print(calculate(2,3))

#lambda parameter : expression
print((lambda a,b : a*a + 2*a*b + b*b)(3,3))

a = (lambda a,b : a*a + 2*a*b + b*b)(3,5)
print(a)


def cube(x):
    return x*x*x
print(cube(3))

print((lambda x : x*x*x)(5))

b = (lambda x : x*x*x)(2)
print(b)
