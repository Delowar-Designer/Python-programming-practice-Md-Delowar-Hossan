# Even Nembers
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

even_numbers =[]
starting = 0
user_input = int(input("Limit: "))
# while starting <= user_input:
#     if is_even(starting):
#         even_numbers.append(starting)
#     starting = starting+1
for num in range(0, user_input +1):
    if is_even(num):
        even_numbers.append(num)

print(f"Even numbers: {even_numbers}")
print("Finished")
