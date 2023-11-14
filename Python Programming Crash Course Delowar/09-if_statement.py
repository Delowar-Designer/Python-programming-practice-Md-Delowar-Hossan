#----if statement in python ----
'''
x = 20
y = 20

# if statement
if x<y:
    #body of if
    print("x is smaller than y")
elif x>y:
    #body of elif
    print("x is greater than y")
elif x==y:
    print("x is equal")
else:
    #body of else part
    print("enter right value")

#program to find out the user is eligible for driving license of not
user_age = int(input("Enter yor age: "))

if user_age >=18 and user_age <=45:
    print("you are eligible for driving license")
elif user_age>=45 and user_age<=65:
    print("your age is too high so chances are not so good to getint a driving license")
else:
    print("soory your age is to young")
'''

#nested if statement
x =10
if x>5:
    print("x is more than 5")
    #nestd if
    if x>10:
        print("x is mre than 10")
    else:
        print("x is not more than 5")
else:
    print("put wright valu")