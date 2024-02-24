# Python Project 7.1 Contact Book App Using
Contact = {}

def ShowFunction():
    print("Name \t Contact")
    for key in Contact:
        print("{} \t {}".format(key, Contact.get(key)))

while True:
    choice = int(input("1. Add New Contact \n"
                   "2. Search the Contact \n"
                   "3. Display the Contact \n"
                   "4. Edit The Contact \n"
                   "5. Delete The Contact \n"
                   "6. Exit \n"
                   "Please Write Number Between 1-6: "))

    if choice == 1:
        name = input("Add Your Contact Name: ")
        phone = input("Add Your Phone Number: ")
        Contact[name] = phone

    elif choice == 2:
        contact_name = input("Search the Contact: ")
        if contact_name in Contact:
            print(contact_name, "Contact number is ", Contact[contact_name])
        else:
            print("Contact Not Found")

    elif choice == 3:
        if not Contact:
            print("Contact book is empty")
        else:
            ShowFunction()

    elif choice == 4:
        edit_contact = input("Edit Your Contact: ")
        if edit_contact in Contact:
            phone = input("Change Your Number: ")
            Contact[edit_contact] = phone
            print("Contact Updated Successfully ")
            ShowFunction()
        else:
            print("Name is Not Found")

    elif choice == 5:
        del_contact = input("which Contact Do You Want To Delete?: ")
        if del_contact in Contact:
            deleted_confirm = input("do you want to delete this contact y/n: ")
            if deleted_confirm.lower() == "y":
                Contact.pop(del_contact)
                ShowFunction()
        else:
            print("the name is not found in the contact")

    elif choice == 6:
        break

    else:
        print("Invalid Choice! Please select a number between 1 and 6.")
