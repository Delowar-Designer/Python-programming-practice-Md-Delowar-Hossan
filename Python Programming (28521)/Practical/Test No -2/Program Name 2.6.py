# Great and Poem assessment program with number input of a student in one subject
def grade(m):
    if(m>+80):
        return "A+"
    elif m>75:
        return "A"
    elif m>70:
        return "A-"
    elif m>65:
        return "B+"
    elif m>60:
        return "B"
    elif m>55:
        return "B-"
    elif m>50:
        return "C+"
    elif m>45:
        return "C"
    elif m>40:
        return "D"
    else:
        return "F"

def point(m):
    if (m > +80):
        return "4"
    elif m > 75:
        return "3.75"
    elif m > 70:
        return "3.5"
    elif m > 65:
        return "3.25"
    elif m > 60:
        return "3"
    elif m > 55:
        return "2.75"
    elif m > 50:
        return "2.5"
    elif m > 45:
        return "2.25"
    elif m > 40:
        return "2"
    else:
        return "0"

m = int(input("Enter the a Marks = "))
print("Your Grade = ",grade(m),"and point = ",point(m))