import json
import os

class ContactsManager: 
    '''Class to manage contacts'''
    def __init__(self):
        self.contacts = []
        self.json_file_path = os.path.join(os.path.dirname(__file__), 'contacts.json') # Variable to store the path of the contacts.json file
        self.load_contacts()

    def load_contacts(self):
        '''Loads all contacts from the JSON file'''
        if os.path.exists(self.json_file_path): # Checks if the file exists
            with open(self.json_file_path, "r") as file: # Reads the file
                self.contacts = json.load(file) # Loads the file into the contacts list
        else:
            self.contacts = []

    def save_contacts(self):
        '''Saves all contacts to the JSON file'''
        with open(self.json_file_path, "w") as file:  # Open in write mode
            json.dump(self.contacts, file, indent=4) # Write the contacts list to the file

    def add_contact(self, name, email, preferred_time="08:00 AM"):
        '''Add a new contact'''
        contact = {
            "name": name,
            "email": email,
            "preferred_time": preferred_time
        }
        self.contacts.append(contact) # Adds new contact
        self.save_contacts()  # Save the updated contacts list to the JSON file

    def remove_contact(self, name):
        '''Remove a contact givent it's name'''
        self.contacts = [c for c in self.contacts if c["name"] != name]
        self.save_contacts()  # Save the updated contacts list to the JSON file

    def get_contacts(self):
        '''Return the list of contacts'''
        return self.contacts

    def list_contacts(self):
        '''List all contacts'''
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
