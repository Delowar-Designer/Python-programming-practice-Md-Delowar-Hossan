# Description of the working a yield kyoward
# creating a function
def generatorExample():
    yield "D"
    yield "E"
    yield "L"
    yield "W"
    yield "A"
    yield "R"
# calling the genneratorExample() function which is created above
result = generatorExample()
# Traversing in the above result(generator object)
for k in result:
    # Printing the corresponding value
    print(k)
