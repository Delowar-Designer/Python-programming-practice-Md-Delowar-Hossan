# Python Project 7 Contact Book App Using
Contact = {}

def ShowFuntion():
    print(Contact.items())
    print("Name \t Contact")
    for key in Contact:
        print("{} \t {}".format(key,Contact.get(kye)))
while True:
    choice = int(input("1. Add New Contact \n"
                   "2. Search the Contact \n"
                   "3. Display the Contact \n"
                   "4. Edit The Contact \n"
                   "5. Delete The Contact \n"
                   "6. Exit \n"
                   "Please Writh Number Between 1-6: "))

    if choice == 1:
        name = input("Add Yourr Contact Name: ")
        phone = input("Add Your Phone Number: ")
        Contact[name] = phone

    elif choice == 2:
        ContactName = input("Search the Contact: ")
        if ContactName in Contact:
            print(ContactName, "Contact number is ",Contact[ContactName])
        else:
            print("Not Found the Contact")

    elif choice == 3:
        if not Contact:
            print("Contact book is empty")
        else:
            ShowFuntion()

    elif choice == 4:
        EditContact = input("Edit Your Contact: ")
        if EditContact in Contact:
            phone = input("Change Your Number: ")
            Contact[EditContact] = phonne
            print("Contact Updated Successfully ")
            ShowFuntion()
        else:
            print("Name is Not Found")

    elif choice == 5:
        Del_Contact = input("which Conntact Do You Want To Delet?: ")
        if Del_Contact in Contact:
            DeletedConfirm = input("do you want to delete this contact y/n")
            if DeletedConfirm == "y" or DeletedConfirm == "Y":
                Contact.pop(Del_Contact)
            ShowFuntion()
        else:
            print("the name is not found in the contact")


    else:
        break



