# ACIT4420-MorningMessage

**ACIT4220-MorningMessage** is a morning greeting package developed as a part of the ACIT4420 course and mandatory assigment. The package includes four python files which includes contact_manager.py, message_generator.py, message_sender.py and logger.py. Additonaly the program has a `__main__.py` entrypoint, an `__init__.py` file to mark it as module, a log_message.txt file for logging and a JSON file were the contacts are stored.
## Table of Contents
- [Features](#features)
- [Installation Manual](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Files](#key-files)
- [License](#license)
  
## Features
- Interactions with contacts including adding, removing and delivery of greeting messages.
- Easy to install and run using a command-line interface.
- Educational for those learning Python and package management.
- Modular design for easy extension and maintenance.
  
## Installation Manual

Follow these simple steps to install and set up the project:

1. **Clone the Repository**

Firstly, clone the repository from GitHub (or download the package manually):

```bash
git clone https://github.com/bowcarl/ACIT4420-MorningMessage.git
cd ACIT4420-MorningMessage
```
2. **Create a virtual environment**

Furthermore, It's recommended to create a virtual environment to isolate the project dependencies. Continue and run the following commands:

```bash
python3 -m venv morningenv
source morningenv/bin/activate # or with windows use `morningenv\Scripts\activate`
```

3. **Install the Package**

With your virtual environment set up, install the project using the pip tool:

```bash
pip install -e .
```

## Usage
Once the package is installed you only need to run this command in your preffered terminal:
```bash
morning_greetings
```
This will launch a menu (from the **__main__.py** entrypoint) where you can choose between four options, which loops until the user exits the code:
1. **Add a Contact**
2. **Remove a Contact**
3. **Send Morning Greeting Messages**
4. **Exit the code**

Simply decide upon an option and follow the on-screen instructions for further guidance.

Modules included:

### 1. contact_manager.py
A simple class managing contacts stored in a JSON file, with built in functions like add_contact, remove_contact(), load_contacts(), save_contacts() and list_contacts().

### 2. message_generator.py
Generates a personalized morning greeting message for a specific user throught the function generate_message().

### 3. logger.py
Logs the morning greeting message for a specific user through the function log_message().

### 4. message_sender.py
Sends a greeting message to a specific email address, raising an error if the email is not provided throught the function send_message().


## Project Structure
```
ACIT4420-MorningMessage/
│
├── morning_greetings/
|   ├── __pyache__.py
|       ├── (...).py
|   ├── morning_greetings.egg-info
|       ├── (...).py
│   ├── __init__.py
│   ├── __main__.py                # Entry point for the module
│   ├── contact_manager.py
|   ├── contacts.json
|   ├── logger.py
|   ├── message_generator.py
|   ├── message_log.txt
|   ├── contact_manager.py
│   └── message_sender.py
│
├── setup.py                   # Installation script
└── README.md                  # Project documentation (this file)
```
### Key Files
- **`main.py`**: Contains the main function that launces the option menu.
- **`setup.py`**: Scripts for installing the package.
## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/shailendrabhandari/project_game/blob/main/LICENSE) file for details.

