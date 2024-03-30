#23 Recursion in Python
import sys
sys.setrecursionlimit(50000)
print((sys.getrecursionlimit()))
i=0
def a():
    global i
    i+=1
    print("Hello",i)
    a()

a()