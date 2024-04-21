# Practice Problem
first_Name = input('Write your First Name: ')
second_Name = input('Write your Second Name: ')

full_name = f"{first_Name} {second_Name}"

print('Your Full Name is :',full_name)
print("Title format:",full_name.title())
print("Upper Case format:",full_name.upper())

change_second_name = input('Relace your Second Name: ')
new_full_name = full_name.replace(second_Name,change_second_name)

print(full_name, "Your new Full Name is",new_full_name)