#21 Pass List to a Function in Python
lst = [1,2,3,4,5,6,7,8,9]
def nothing(lst1):
    print(lst1)

nothing(lst)

lst = [1,2,3,4,5,6,7,8,9]
def a(lst1):
    even=0
    odd=0
    for i in lst1:
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("odd: {} and even: {}".format(odd, even))
a(lst)