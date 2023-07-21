import json





"""load from file json to list contacts"""
def load(DATA_FILE):
    with open(DATA_FILE, 'r') as json_file:
         return json.load(json_file)



"""save contact list to file"""
def save(DATA_FILE,contacts):
    with open(DATA_FILE,'w') as json_file:
        json.dump(contacts,json_file)



"""add a new contact to contacts list"""
def add_new_contact(contacts):
    contacts.append({"name":input("Please enter full name:\n"),"cell_phone":input("Please enter the cell phone number:\n")})
    print("Contact successfully added")
    



"""print all the contacts """
def print_all_contacts(contacts):
    print(contacts)




"""delete contact by name"""
def delete_contact(contacts):
    contact_to_search = input("Which name whould you like to delete?")
    for contact in contacts:
        if contact["name"] == contact_to_search:
            print(f"The following details have been deleted")
            print(f"full name: {contact['name']}, cell phone: {contact['cell_phone']}")
            contacts.remove(contact)
            return
    print(f"{contact_to_search} Not Found")





"""search contact by name"""
def search_contact(contacts):
    contact_to_search = input("Which name whould you like to delete?")
    for contact in contacts:
        if contact["name"] == contact_to_search:
             print(f"Found, name: { contact['name']}  , cell phone: { contact['cell_phone']}")
             return
    print(f"Not Found {contact_to_search}")
