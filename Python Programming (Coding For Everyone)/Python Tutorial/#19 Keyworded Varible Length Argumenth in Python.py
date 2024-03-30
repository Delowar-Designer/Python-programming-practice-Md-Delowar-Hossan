#19 Keyworded Varible Length Argumenth in Python
def student(name, **details):
    print(name)
    print(details)
    for i,j in details.items():
        print(i)
        print(j)
student("Delowar",roll=342,marks=3,phon=300838903)
