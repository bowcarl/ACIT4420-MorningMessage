import datetime
import os
def log_message(contact, message):
    '''Log a message to a file'''
    if not contact:
        raise ValueError("Contact is missing")
    file_path = os.path.join(os.path.dirname(__file__), 'message_log.txt') # Variable to store the path of message_log.txt
    with open(file_path, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Send to {contact}['name']: {message}\n")
