#7 swap first and last element in a List
my_list = [1,2,3,4]
print(my_list)

def swaplist(my_list):
    my_list[0], my_list[-1] = my_list[-1],my_list[0]
    return my_list
swaplist(my_list)
print(my_list)
