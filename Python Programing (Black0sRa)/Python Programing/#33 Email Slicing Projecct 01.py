# Email Slicing Projecct
email_name = input("Enter your e-mail: ").strip()
user_name = email_name[:email_name.index('@')]

domain_name = email_name[email_name.index('@')+1:]

print(f'User Name: {user_name}\n'
      f'Domain Name: {domain_name}')