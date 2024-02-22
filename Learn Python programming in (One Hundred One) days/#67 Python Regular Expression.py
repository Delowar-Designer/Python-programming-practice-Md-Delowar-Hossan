#67 Python Regular Expression
import re
text = "1 The rain in Spain"
pattern = "[a-z]"
a = re.findall(pattern,text)
print(a)

pattern = "^1"
b = re.findall(pattern,text)
if b:
    print("Yes, 1 is a special characters")
else:
    print("np, 1 is not special characters")

pattern = "Spain$"
c = re.findall(pattern,text)
if c:
    print("Yes we find spesial characters")
else:
    print("nope, special characters not finded")