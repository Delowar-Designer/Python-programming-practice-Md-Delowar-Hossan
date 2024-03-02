# Dictionary
dictionaryExample = {
    "Name": "Delowar",
    "id" : "602826",
    "year": "5rd"
}

print(dictionaryExample)
print(dictionaryExample['id'])
dictionaryExample["Name"] = "Mitu"
print(dictionaryExample['Name'])
print(dictionaryExample.get('Name'))

for x in dictionaryExample:
    print(dictionaryExample[x])

for x in dictionaryExample.values():
    print(x)

for x in dictionaryExample.items():
    print(x)

for x, y in dictionaryExample.items():
    print(x,y)
    print(x)
    print('-')
    print(y)

del dictionaryExample["Name"]
print(dictionaryExample)