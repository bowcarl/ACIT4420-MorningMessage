import json
import os

class ContactsManager:
    def __init__(self):
        self.contacts = []
        self.json_file_path = os.path.join(os.path.dirname(__file__), 'contacts.json')
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.json_file_path):
            with open(self.json_file_path, "r") as file:
                self.contacts = json.load(file)
        else:
            self.contacts = []

    def save_contacts(self):
        with open(self.json_file_path, "w") as file:  # Open in write mode
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, email, preferred_time="08:00 AM"):
        contact = {
            "name": name,
            "email": email,
            "preferred_time": preferred_time
        }
        self.contacts.append(contact)
        self.save_contacts()  # Save the updated contacts list to the JSON file

    def import_contacts(self, json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
            for contact in data:
                self.contacts.append(contact)
        self.save_contacts()  # Save the updated contacts list to the JSON file

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c["name"] != name]
        self.save_contacts()  # Save the updated contacts list to the JSON file

    def get_contacts(self):
        return self.contacts

    def list_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")