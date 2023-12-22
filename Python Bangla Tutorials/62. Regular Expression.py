# Regular Expression
import re
pattern = r"Colour"
if re.match(pattern, "Colour Red is a colour, I love red colour"):
    print("Match found")
else:
    print("Match not found")


pattern = r"Colour0"
if re.search(pattern, "Red is a Colour0, I love red colour"):
    print("Match found")
else:
    print("Match not found")

pattern = r"Delowar"
print(re.findall(pattern, "Delowar Red is a Colour0, I love Delowar red colour"))


pattern1 = r"colour"
text = "My favourite colour is Red."
chak = re.search(pattern1, text)
if chak:
    print("Match found Start: ", chak.start())
    print("Match Found End: ", chak.end())
    print("Match found Character: ", chak.group())
    print("Match found span: ", chak.span())
