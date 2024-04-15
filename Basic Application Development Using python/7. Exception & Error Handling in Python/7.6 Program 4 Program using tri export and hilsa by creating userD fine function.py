# Program using tri export and hilsa by creating userD fine function
# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        # Floor Divison : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry! You are dividing by zero")
    else:
        print("Yeah! your answer is:",result)
# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)