#4 Python Interview Question and Answer
lst = [2, 4, 5,6,1,9]
diff_list=[]
done = []
for i in lst:
    done.append(i)
    for j in lst:
        if i == j or (j in done):
            pass
        else:
          diff_list.append(j-i)

print(diff_list)
diff_list.sort(reverse=1)
print(diff_list[0])