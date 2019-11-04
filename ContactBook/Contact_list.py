import pickle
import os

UserInput = """
1. Add Contact
2. Search Contact
3. Exit
"""


class Contact(object):

    def __init__(self, name, address, phone, email):  # creating instances of class contact
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return "{},{:>15},{:>15},{:>15}".format(self.name, self.address, self.phone, self.email)


class ContactBook(object):

    def __init__(self,contactBook):
        self.contactBook = contactBook
        self.contacts = {}
        if not os.path.exists(self.contactBook):
            file_pointer = open(self.contactBook, 'wb')
            pickle.dump({}, file_pointer)
            file_pointer.close()
        else:
            with open(self.contactBook, 'rb') as contact_list:
                self.contacts = pickle.load(contact_list)

    def add(self):
        name, address, phone, email = self.getData()
        if name not in self.contacts:
            self.contacts[name] = Contact(name, address, phone, email)
        else:
            print("Contact already exist.")

    def getData(self):
        name = input("Contact Name: ")
        address = input("Contact Address: ")
        phone = input("Phone Number: ")
        email = input("Email Address: ")
        return name, address, phone, email

    def search(self):
        name = input("Insert Contact Name: ")
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print("Contact not found!")

    def __str__(self):
        return UserInput


def main():
    cont = ContactBook('Contacts.data')
    selection = ''
    while selection != '3':
        print(cont)
        selection = input("Enter Selection: ")
        if selection == '1':
            cont.add()
        elif selection == '2':
            cont.search()
        elif selection == '3':
            print("Exiting Contact Book!")
        else:
            print("Enter valid selection!")

if __name__ == '__main__':
    main()
