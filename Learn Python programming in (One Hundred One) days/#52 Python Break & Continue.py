#52 Python Break & Continue
list = ["Delowar",'Mitu',"Joty",1,2,3,4,5,6,7,8,9,10]
for x in range(len(list)):
    if x == 4:
        break
    print('Break',x)
for y in range(len(list)):
    if y == 3:
        continue
    print(y,"Continue")