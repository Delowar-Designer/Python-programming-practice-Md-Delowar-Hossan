#৬- ফাংশন ব্যবহার করে কোনো স্ট্রিং-কে রিভার্স অর্ডারে সাজানোর প্রোগ্রাম।
#6- Program to sort a string in reverse order using functions.
def string_reverse(str1):
    rstr1=''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index-1]
        index = index-1
    return rstr1
print(string_reverse('000123456789'))
print(string_reverse("Delowar.Designer"))
print(string_reverse("rengiseD.rawoleD"))