contacts = {}

while True:
    print("\nWelcome to Contact Book App ::")
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit from Contact App')

    choice = input("Enter Your Choice Here :: ")

    if choice == "1":
        name = input("Enter Your Name here : ")
        if name in contacts:
            print(f'Contact name {name} already exists.')
        else:
            age = input("Enter age here : ")
            email = input("Enter email here : ")
            mobile = input("Enter Mobile Number here : ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact Name {name} has been created successfully.')

    elif choice == "2":
        name = input("Enter Contact Name to view : ")
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age: {contact["age"]}, Email: {contact["email"]}, Mobile: {contact["mobile"]}')
        else:
            print("Contact Not Found")

    elif choice == "3":
        name = input("Enter the Name you want to Update : ")
        if name in contacts:
            age = input("Enter Updated age here : ")
            email = input("Enter Updated email here : ")
            mobile = input("Enter updated Mobile Number here : ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact Name {name} has been updated successfully.')
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter contact name to delete : ")
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} deleted successfully.')
        else:
            print("Contact Not Found!")

    elif choice == "5":
        search_name = input("Enter Contact Name to Search : ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() == name.lower():
                print(f'Found Name: {name}, Age: {contact["age"]}, Mobile Number: {contact["mobile"]}, Email: {contact["email"]}')
                found = True
                break
        if not found:
            print("No Contact found with that name.")

    elif choice == "6":
        print(f'Total Contacts are : {len(contacts)}')

    elif choice == "7":
        print("Good Bye! Closing the Program.")
        break

    else:
        print("Invalid Input")


                