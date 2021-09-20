class AddressBook:

    def create_contact(self):
        first_name = input("Enter first name:\t")
        last_name = input("Enter last name:\t")
        address = input("Enter address:\t")
        city = input("Enter city:\t")
        state = input("Enter state:\t")
        zip = input("Enter zip code:\t")
        phone_number = input("Enter phone number:\t")


if __name__ == "__main__":
    print("Welcome to Address Book")
    book = AddressBook()
    book.create_contact()


