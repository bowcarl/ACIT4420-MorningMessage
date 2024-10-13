from . import contact_manager
from . import message_sender
from . import logger
from . import message_generator

Contacts = contact_manager.ContactsManager()

def send_messages():
    Contacts.list_contacts()
    if not Contacts.contacts:
        print("No contacts found. Please add some contacts first.")
        return
    for people in Contacts.contacts:
        message = message_sender.send_message(people["email"], message_generator.generate_message(people["name"]))
        logger.log_message(people['name'], message)

def main():
    global Contacts

    while True:
        name = input("Name: ")
        email = input("Email: ")
        preferred_time = input("Preferred Time: ")
        if not any(c["email"] == email for c in Contacts.contacts):
            Contacts.add_contact(name, email, preferred_time)
            break
        else:
            print("Email is already occupied. Start over.")
    send_messages()


if __name__ == "__main__":
    main()