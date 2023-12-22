# Search and Replace
import re
pattern = r"Delowar"
text1 = "My name is Delowar and My Favorite colour is Red.I love Delowar blue colour as Well"
text2 = re.sub(pattern,"Mitu", text1, count=1)
print(text2)