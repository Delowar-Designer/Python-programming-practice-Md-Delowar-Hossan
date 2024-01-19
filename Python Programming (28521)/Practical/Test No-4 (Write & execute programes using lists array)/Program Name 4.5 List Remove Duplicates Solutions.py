# Program Name 4.5 List Remove Duplicates Solutions
# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
# Driver Code
duplicate = []
duplicate = input("Enter Digit or Alphabetic using Conna = ")
print(duplicate)
print("Remove duplicate elements:",Remove(duplicate))