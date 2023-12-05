# ২- ফাংশন ব্যবহার করে দুটি সংখ্যার মধ্যে বৃহত্তম সংখ্যাটি নির্ণয়ের প্রোগ্রাম।
# 2- Program to find the largest number between two numbers using functions.
def Largest():
    Number1=int(input("Enter the value of 1st Number:"))
    Number2=int(input("Enter the value of 2nd Number:"))
    if(Number1>Number2):
        print("Largest is Number1 & it is=",Number1)
    else:
        print("Largest is Number2 & it is=",Number2)
Largest()