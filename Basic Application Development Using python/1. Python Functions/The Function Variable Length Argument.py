#The Function Variable Length Argument
def Show(*Numbers):
    print(type(Numbers))
    print(Numbers)
Show(50,60,70,80,90)


#The Function Variable Length Argument2
def Show(**Numbers):
    print(type(Numbers))
    print(Numbers)
Show(x=50,y=60,z=70)

