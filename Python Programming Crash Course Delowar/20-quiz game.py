#---Quiz app in Python -----
q1 = '''Wat is a correct syngax to outqut "Hello World" in Python?
a) echo("Hello World")
b) p("Hello World")
c) Print("Hello World")
d) echo "Hello Warld
'''
q2 = '''Which one is Not a legal variable name?
a) my_var
b) my-var
c) _myvar
d) Myvar
'''
q3 = '''What is the correct file extension for python files?
a) .pyth
b) .pt
c) .py
d) .pyt
'''
q4 = '''Which method can be uded to return a string in upper case letters?
a) upper()
b) toUpperCase()
c) uppercase()
d) upperCase
'''
q5 ='''Which operator is used to multiply numbers?
a) X
b) *
c) # 
d) %
'''


# CREATE DICTIONARY
questions = {q1:"c",q2:"a",q3:"c",q4:"a",q5:"b"}
name = input("Enter Your Name: ")
print("Hello",name,"Welome to the quiz")

score = 0
for i in questions:
    print(i)
    skip_question = input("Do You want to skip this question: please type (Yes/No) :")
    if skip_question == "Yes" or skip_question == "yes":
        continue
    answer = input("Enter the correct answer (a/b/c/d): ")
    
    if answer == questions[i]:
        print("Correat Answer, You got 1 point")
        score = score+1
        print("Current Score is: ",score)
    else:
        print("Wrong answer,You lost 1 point")
        score = score-1
    skip_quiz = input("Do You Want to exit this quiz: please type (Yoes/No) :")
    if skip_quiz == "Yes" or skip_quiz == "yes":
        break

print("Final score is",score)



