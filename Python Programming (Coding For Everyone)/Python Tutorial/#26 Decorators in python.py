#26 Decorators in python
def test1():
    print("in test")

test2=test1
del test1
test2()
def test3(num):
    if num==0:
        return print
    if num ==1:
        return sum
ret=test3(0)
print(ret)

def test4(func):
    func("in test function")
test4(print)

def test5(func):
    def exec():
        print("first line of exec")
        func()
        print("3rd line of exec")
    return exec
@test5
def my_func():
    print("Please to my chake")

#my_func = test5(my_func)
my_func()