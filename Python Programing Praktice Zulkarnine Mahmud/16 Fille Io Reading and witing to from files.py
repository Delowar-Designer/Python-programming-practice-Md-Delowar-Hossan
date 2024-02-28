
# 16 Fille Io Reading and witing to from files
with open("Delowar.txt", mode="r") as s_file:
    words_all = []
    for line in s_file.readlines():
        words = line.strip().split(" ")
        words_all += words
        #words = line.split(" ")
    unique_words = set(words_all)
    print(len(unique_words))
    print(words_all)
    print(len(words_all))

    with open("unique_words.txt", mode = "w") as write_file:
        for item in sorted(unique_words):
            write_file.write(item)
            write_file.write("\n")

        # print(line.strip())
       # print(line, end="")

print("Finished")
