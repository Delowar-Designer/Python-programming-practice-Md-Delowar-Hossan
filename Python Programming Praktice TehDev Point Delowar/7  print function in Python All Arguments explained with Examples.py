#  print function in Python | All Arguments explained with Examples
'''print('My name is', 'Delowar', "I love \"Python")
print('My name is', 'Delowar', sep= '$ ', end='-----')
print('I live in Germany')

with open('python.txt','w') as file:
    print('i born in Bangladesh', 'I love my country', sep='. ', end='-----')'''

import time
for i in range(10):
    print(i, end = '---', flush=True)
    time.sleep(1)