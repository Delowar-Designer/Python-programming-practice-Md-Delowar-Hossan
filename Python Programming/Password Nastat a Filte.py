password=int(input("enter the for password="))
if password==99225:
    a=int(input("plise enter number A="))
    b=int(input("plise enter number B="))
    c=int(input("plise enter number C="))
    if a>b and b>c:
        print ("enter is largest A =",a)
    elif b>a and b>c:
        print("enter is largest B =",b)
    else:
        print ("enter is largest C =",c)
        
else:
    print("wrong Password=",password)
