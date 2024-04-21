# Logical Operators
has_PC = True
has_resources = True

if has_PC and has_resources:
    print("You can learn Python")


has_PC = True
has_resources = False

if has_PC or has_resources:
    print("You can learn Python")

has_phone = False
if (has_PC or has_phone) and not has_resources:
    print("Your can learn Python Coding")