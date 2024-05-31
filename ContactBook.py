class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
        self.contacts.append(contact)
        print(f"Contact {name} added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term in contact['name'] or search_term in contact['phone']]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                print(contact)

    def update_contact(self, name, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact['name'] == name:
                if phone:
                    contact['phone'] = phone
                if email:
                    contact['email'] = email
                if address:
                    contact['address'] = address
                print(f"Contact {name} updated.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            contact_book.update_contact(name, phone if phone else None, email if email else None, address if address else None)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
