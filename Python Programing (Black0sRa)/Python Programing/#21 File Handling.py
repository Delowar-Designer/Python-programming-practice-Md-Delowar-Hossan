# File Handling
'''file = open('poem.txt', 'r')
# print(file.readlines())
for i in file:
    print(i.strip().split())

file.close()'''

'''file = open('poem.txt', 'w')
file.write("HAHA! I hacked your file, \n Dont use your file directly. ")

# read
file = open('poem.txt', 'r')
print(file.read())
file.close()

with open('poem.txt', mode='r') as read_file:
    all_word = []
    for word in read_file:
        new_word = word.strip().split()
        all_word += new_word
    unique_list = set(all_word)
    print(len(all_word))
    print(len(unique_list))

    with open("unique_words.txt", mode='w') as write_file:
        for item in sorted(unique_list):
            write_file.write(item)
            write_file.write("\n")
print("Finished")
'''
import os
os.remove(unique_words.txt)