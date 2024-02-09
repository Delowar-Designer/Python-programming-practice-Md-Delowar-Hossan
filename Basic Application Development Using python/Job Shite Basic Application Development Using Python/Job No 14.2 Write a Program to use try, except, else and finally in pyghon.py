# Write a Program to use try, except, else and finally in pyghon
def div(x,y):
    try:
        result = (x/y)
    except ZeroDivisionError:
        print("Piz give valid numbet")
    else:
        print("Result=",result)
    finally:
        print("The try...except block is finished")
div(10,2)
div(6,0)

