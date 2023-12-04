# Leep Year বের করার প্রোগ্রাম লিখ।
year=int(input("Enter the yer:="))
if ((year%400==0)or((year%4==0)and(year%100!=0))):
    print("This is Leep year=",year)
else:
    print("This is not a Leep year=",year)
    