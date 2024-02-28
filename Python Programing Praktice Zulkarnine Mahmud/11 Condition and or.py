# 11 Condition and or
marks = int(input("what is your marks in programming: "))
the_user_is_good = True
print(the_user_is_good)
def show_grade(grade):
    print(f"You got: {grade}")

if marks > 80 or marks < 10:
    print("You are very good of very bad")
    if marks > 80:
        print(" Excellent")
    else:
        print("No so good!")
else:
    print("You are okay")

print("Finished")