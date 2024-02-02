# List Methods Use in Sort
os = ['Windows','macOS','Linux']
print('Original List:',os)
# List Reverse
os.reverse()
# updated list
print('Updated List:',os)
reversed_list = os[::-1]
print('Updated List:',reversed_list)
for o in reversed(os):
    print(o)
