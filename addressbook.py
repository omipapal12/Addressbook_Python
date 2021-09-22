import logging

from Contact import Contact

logging.basicConfig(filename="addressbook.log",filemode='w',level=logging.INFO)


class AddressBook:

    def __init__(self):
        self.contact_list = []

    def add_contact(self):
        contact = Contact.create_contact()
        self.contact_list.append(contact)

    def display_contact(self):
        contacts = "".join(str(contact) for contact in self.contact_list)
        print(contacts)

    def edit_contact(self):
        user_data = input("Enter The First Name That You Want To Edit\n")
        for contact in self.contact_list:
            if contact.first_name == user_data:
                enter_value = int(input(
                    "Edit Options\n 1. First Name 2. Last name 3. Address 4. city 5. state 6.zip 7. Phone number 8.Email\n"))
                if enter_value == 1:
                    first_name = input("Enter new first name\n")
                    contact.first_name = first_name
                elif enter_value == 2:
                    last_name = input("Enter new last name\n")
                    contact.last_name = last_name
                elif enter_value == 3:
                    address = input("Enter new address\n")
                    contact.address = address
                elif enter_value == 4:
                    city = input("Enter new city\n")
                    contact.city = city
                elif enter_value == 5:
                    state = input("Enter new state\n")
                    contact.state = state
                elif enter_value == 6:
                    zip = input("Enter new zip\n")
                    contact.zip = zip
                elif enter_value == 7:
                    phone_number = input("Enter new phone number\n")
                    contact.phone_number = phone_number
                elif enter_value == 8:
                    email = input("Enter new email\n")
                    contact.email = email
                else:
                    print("Please give the valid option")
            else:
                print("Please give the valid name")

if __name__ == "__main__":
    print("Welcome to Address Book")
    book = AddressBook()
    while True:
        try:
            preference = int(input(
                "Enter what operation you want to perform\n 1.Add Contact 2. Display Contact 3.Edit Contact 4.Exit\n"))
            if preference == 1:
                book.add_contact()
            elif preference == 2:
                book.display_contact()
            elif preference == 3:
                book.edit_contact()
            elif preference == 4:
                print("Successfully closing Address Book")
                exit(0)
            else:
                logging.warning("Invalid option")
        except ValueError:
            logging.warning("Invalid Option selected")