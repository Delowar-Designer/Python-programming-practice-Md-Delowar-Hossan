# Program scarch findall split sub builtt in methods in python RegEx
import re
txt = 'The rain in Spain'
x = re.findall("ai",txt)
print(x) # Output:("ai",txt)
x = re.findall("Portuagl",txt)
print(x) # output []
x = re.search("\s", txt) # ouput the first white- space character is located isn position 3
print("The first white_space character is located in position:", x.start())
x = re.search("Portugal", txt)
print(x) # output None
x = re.split("\s",txt)
print(x) # output ['The', 'rain', 'in', spain']
x = re.split("\s",txt,1)
print(x) # output ['The', 'rain in Spain']
x = re.sub("\s","9",txt)
print(x) #outtput The9rain9in9Spain
x = re.search("ai",txt)
print(x) # output <re.Match object; span=(5, 7), match='ai'>
