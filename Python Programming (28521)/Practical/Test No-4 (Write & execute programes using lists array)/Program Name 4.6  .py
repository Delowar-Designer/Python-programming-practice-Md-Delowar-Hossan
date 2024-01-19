# Write a program to find even and odd numbers between numbers up to 100 in 1 hand using list
even = []
odd = []
i = 1
while i <= 100:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
    i = i+1
print("Even Numbers= ",even)
print("Odd Numbers= ",odd)