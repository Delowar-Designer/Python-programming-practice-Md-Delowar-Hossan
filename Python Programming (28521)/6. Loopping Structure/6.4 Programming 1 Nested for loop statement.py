# Nested for loop statement

"""for iterating_variable in sequence:
    for iterating_variable in sequence:
        statements(s)
    statements(s)"""

num_list = [1,2,3,4,5,6,7]
alpha_list = ['a','b','c']

for number in num_list:
    print(number)
    for letter in alpha_list:
        print(letter)