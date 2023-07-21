import json
from helper import add_new_contact, delete_contact, search_contact, print_all_contacts, load,save

contacts = []
DATA_FILE = 'contacts.json'

"""menu """
def menu():
    print()
    print("PHONE BOOK")
    print("what would you like to do?")
    print()
    print("1 - Add new contact")
    print("2 - Print all contacts")
    print("3 - Delete contact by name")
    print("4 - Search contact by name")
    print("5 - EXIT")
    print()
    user_selection = input("Your selection is: ")
    return int(user_selection)



def main():
   contacts = load(DATA_FILE)
   user_selection = menu()
   while user_selection !=5:
       if user_selection == 1: add_new_contact(contacts)
       if user_selection == 2: print_all_contacts(contacts)
       if user_selection == 3: delete_contact(contacts)
       if user_selection == 4: search_contact(contacts)
       user_selection = menu()
   save(DATA_FILE, contacts)




if __name__ == "__main__":
    main()