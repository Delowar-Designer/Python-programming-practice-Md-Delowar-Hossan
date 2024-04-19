# Description of the working procedure of RegEx in python
'''import re

x = re.sub(r'c.t','X''tac tin cat abc;tuv acute')
print(x)
'''
'''gk = df.groupby('Team')
gk.first()'''
'''import re
re.findall('^PYTHON','PYTHON is fun.')
['PYTHON']'''

#import re
#text = '''
#Python is great.
#Python is the fastest growing
#major programming language in
#the world.
#Pythonistas thrive'''
#re.findall('^Python',text)
#[]
#re.findall('^Python', text, re.MULTILINE)
#['PYthon','Python','Python']

import re
my_string = "purple alice @ google.com, blah monkey bob @ abc.com blah dishwasher"
temp = my_string.split(',')
for phrase in temp:
    result = re.match("([\w\.-]+)@([\w\.-]+)", phrase)
    print(result)
