from . import contact_manager
from . import message_sender
from . import logger
from . import message_generator

Contacts = contact_manager.ContactsManager()

def send_greetings():
    '''Send morning greetings to all contacts'''
    Contacts.list_contacts()
    if not Contacts.contacts: # Checks if there are no contacts in contacts.json
        print("No contacts found. Please add some contacts first.")
        return
    for people in Contacts.contacts: # Iterates and prints out the name and email of each contact
        message = message_sender.send_message(people["email"], message_generator.generate_message(people["name"]))
        logger.log_message(people['name'], message)
        
def choices():
    '''Prints out the choice menu'''
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Send Messages")
    print("4. List contacts")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    '''Main function and entrypoint'''
    global Contacts
    while True: # Loops until the user exits
        choice = choices()
        if choice == '1':
            while True:
                name = input("Name: ")
                email = input("Email: ")
                preferred_time = input("Preferred Time: ")
                if not any(c["email"] == email for c in Contacts.contacts): # Checks if the email is unique
                    Contacts.add_contact(name, email, preferred_time)
                    print(f"Contact added successfully.\n{Contacts.list_contacts()}")
                    break 
                else:
                    print("Email is already occupied. Start over.")
        elif choice == '2':
            Contacts.list_contacts()
            email = input("Which contact do you want to remove? ")
            if any(c["email"] == email for c in Contacts.contacts): # Checks if the email exists in contacts.json
                Contacts.remove_contact(email)
            else:
                print("The contact you entered was not found.")
        elif choice == '3':
            send_greetings() # Calls the send_greetings function
        elif choice == '4':
            Contacts.list_contacts()
        elif choice == '5':
            exit() # Exits the program
        else:
            print("Invalid choice. Please enter a valid option (1-5).")
