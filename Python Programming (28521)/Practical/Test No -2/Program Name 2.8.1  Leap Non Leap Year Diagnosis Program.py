#  Leap Non Leap Year Diagnosis Program 2
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# ইনপুট নেওয়া
year = int(input("Enter a year: "))

# লিপ ইয়ার কিনা তা পরীক্ষা এবং প্রিন্ট করা
if is_leap_year(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")


