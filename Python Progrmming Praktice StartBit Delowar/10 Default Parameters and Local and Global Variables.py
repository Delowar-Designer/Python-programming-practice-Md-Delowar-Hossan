#10 Default Parameters and Local and Global Variables
# def simpleFunction(num1, num2):
#     print(num1, "_", num2)
# simpleFunction(2, 5)

# def wishCcard(name, wish="Happy Birthday to "):
#     print(wish, name)
# wishCcard("Adam", "Happy Friendship Day")

var = 10
def simpleFunction():
    # global var
    # var = var + 3
    loc = var
    loc = loc + 4
    print(var)
simpleFunction()