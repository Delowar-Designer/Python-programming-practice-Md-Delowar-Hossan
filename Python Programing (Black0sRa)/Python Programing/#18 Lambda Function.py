# Lambda Function
def add(x):
    return 2*x + 2
print(add(2))

num = lambda number : 2 * number + 2
print(num(2))

name = lambda first_name, last_name : str(first_name).strip().title() + str(last_name).strip().title()
print(name("       Mitu     ","        fack Name S   imeia               "))