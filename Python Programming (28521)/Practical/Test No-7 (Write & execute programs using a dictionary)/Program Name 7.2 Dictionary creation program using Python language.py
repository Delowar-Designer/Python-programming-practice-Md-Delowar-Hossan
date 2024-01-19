# Dictionary creation program using Python language
my_dict_one = {'one':1, 'two':2, 'three':3}   # With curly brackets
print("My Dict One:",my_dict_one)

my_dict_two = dict({'one':1, 'two':2, 'three':3})   # with curly brackets in dict()
print("My Dict Two:",my_dict_two)

my_dict_three = dict(one=1, two=2, three=3)   # With dict() and keyword-arguments
print("My Dict Three:",my_dict_three)

my_dict_four = dict(zip(['one', 'two', 'three'], [1,2,3])) # with dict() and lists in zip()
print("My Dict Four:",my_dict_four)

my_dict_five = dict([('one', 1), ('two', 2), ('three',3)]) # with dict(and list of tuples
print("My Dict Five:",my_dict_five)
