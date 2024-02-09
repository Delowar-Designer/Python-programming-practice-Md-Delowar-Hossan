# Write a Program for cheek valid email address in python using RegEx
import re
dpi = "[a-zA-Z)-9]+@[a-zA-Z]+\.(com|net|in)"
def valid(email):
    if re.search(dpi,email):
        print("email is valid")
    else:
        print("email is invlid")
valid("partho2k5@gmail.com")
valid("parth2k5@gmail.co")
valid("delowar.designer@gmail.com")