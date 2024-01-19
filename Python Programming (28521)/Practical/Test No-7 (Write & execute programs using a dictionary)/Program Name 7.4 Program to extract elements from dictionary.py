# Program to extract elements from dictionary
dict_1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
dict_new = dict_1.copy() # make a copy to work with
print("Dict: ",dict_new)

pop_one = dict_new.pop('one',0)  # Remove and return for key 'one'
if(pop_one):
    print("Removed")
else:
    print("Not Found")

pop_seven = dict_new.pop('seven',0) # Remove and return for key 'seven'
if(pop_seven):
    print("Removed")
else:
    print("Not found")
print("Dict after pop: ",dict_new)