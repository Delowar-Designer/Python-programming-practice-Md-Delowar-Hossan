#9 Binary - read, write
#------------------------------
open("binary2.bin","x")

import pickle

file = open("binary2.bin","rb")
data = pickle.load(file)
for i in data:
    print(i)
#print(data)
file.close()


file = open("binary2.bin","wb")
data = ["Shinchan","5","japon"]
pickle.dump(data, file)
file.close()


