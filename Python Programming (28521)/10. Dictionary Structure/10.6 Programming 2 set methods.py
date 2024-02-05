# set methods
marks = {}.fromkeys(['Math','English','Science'],0)
# Output: {"English" : 0, "Math":0,"Science":o}
print(marks)
for item in marks.items():
    print(item)
# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))
