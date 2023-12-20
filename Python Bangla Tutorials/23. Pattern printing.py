# pattern Printing
"""
n = 4
*
**
***
****
"""
n = int(input("Enter a number : "))
for i in range(n+1):
    print(i*"*")



"""
n = 3
*  (2*i-1)
***
*****
"""
for i in range(n+1):
    print((2*i-1)*"*")

"""
n = 3
     *
    **
   ***
  ****
"""
for i in range(1, n+1):
    spaces = " " * (n - i)
    asterisks = "*" * i
    print(spaces + asterisks)


for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()
