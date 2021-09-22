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

if __name__ == "__main__":
    print("Welcome to Address Book")
    book = AddressBook()
    book.add_contact()
    book.display_contact()