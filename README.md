# Telephone Directory 📞

**Version:** 1.0  
**Author:** Ivan Nenadic

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Demo](#demo)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Program](#running-the-program)
- [Usage Instructions](#usage-instructions)
  - [Main Window](#main-window)
  - [Adding a New Contact](#adding-a-new-contact)
  - [Updating an Existing Contact](#updating-an-existing-contact)
  - [Deleting a Contact](#deleting-a-contact)
  - [Searching Contacts](#searching-contacts)
  - [Sorting Contacts](#sorting-contacts)
  - [Filtering by Group](#filtering-by-group)
  - [Importing and Exporting Contacts](#importing-and-exporting-contacts)
  - [Birthday Reminders](#birthday-reminders)
- [Project Structure](#project-structure)
- [Additional Information](#additional-information)
- [Possible Issues](#possible-issues)
- [Planned Extensions](#planned-extensions)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Description

The **Telephone Directory** is a desktop application developed in Python that allows you to manage your contacts efficiently and intuitively. This application provides functionalities for adding, updating, deleting, and searching contacts. It also supports advanced features such as contact grouping, birthday reminders, and an advanced search mechanism.

## Features

- **Add and Update Contacts**: Store essential information like name, email, address, phone number, and additional details such as date of birth, company, notes, website, and social media profiles.
- **Input Validation**: Ensures the correctness of email addresses, phone numbers, dates of birth, and website URLs.
- **Contact Grouping**: Organize contacts into groups (e.g., Family, Friends, Work) for better management and filtering.
- **Advanced Search**: Search contacts based on various criteria such as name, email, phone, company, or group.
- **Birthday Reminders**: Get notified about upcoming birthdays of your contacts.
- **Sorting and Filtering**: Sort contacts by first name or last name and filter them by groups.
- **Import and Export Contacts**: Easily import contacts from or export to a CSV file.
- **User-Friendly Interface**: Intuitive GUI built with Tkinter, making the application easy to navigate and use.

## Demo

*Note: Screenshots or a GIF demonstrating the application can be added here if available.*

## Requirements

- **Python 3.x**: The application is compatible with Python 3.
- **Tkinter**: The standard GUI library for Python.
  - **Note for Linux users**: You might need to install `tkinter` manually:
    - **Ubuntu/Debian**:
      ```bash
      sudo apt-get install python3-tk
      ```
    - **Fedora**:
      ```bash
      sudo dnf install python3-tkinter
      ```
    - **Arch Linux**:
      ```bash
      sudo pacman -S tk
      ```
- **Standard Python Libraries**: No additional installations required; uses `csv`, `os`, `re`, `datetime`, and `tkinter`.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ivo000/Telefonski-imenik.git
Or download the ZIP file and extract it.

Navigate to the Project Directory:

cd telephone-directory
Verify Python Installation:

python3 --version
If Python 3 is not installed, download it from the official website.

Install Tkinter (if necessary):

Follow the instructions under Requirements.
Running the Program
Execute the following command in your terminal or command prompt:

python3 main.py
For Windows users, you might use:

python main.py
Usage Instructions
Main Window
Upon launching, the application displays the main window divided into:

Add / Update Contact: Input fields for contact information.
Search and Sort: Tools for finding and organizing contacts.
Contact Display: A list showing all saved contacts.
Menu Bar: Access to additional functionalities like importing/exporting contacts.
Adding a New Contact
Enter Contact Details:

Required:
Name
Email
Address
Phone Number
Optional:
Group
Date of Birth (format: DD.MM.YYYY)
Company
Notes
Website
Social Media
Save Contact:

Click the "Save" button to add the contact.
Updating an Existing Contact
Select Contact:

Double-click on the contact in the list.
Edit Details:

Modify the information in the input fields.
Update Contact:

Click the "Update" button to save changes.
Deleting a Contact
Method 1:
Select the contact and click "Delete Selected Contact" button.
Method 2:
Use the menu: Edit > Delete Selected Contact.
Searching Contacts
Enter Search Term:

In the "Search" field, type the keyword.
Select Criterion:

From the "By:" dropdown, choose the field to search (e.g., Name, Email).
View Results:

The contact list updates automatically to show matching contacts.
Sorting Contacts
Use the "Sort by:" dropdown to sort contacts by First Name or Last Name.
Filtering by Group
Select a group from the "Filter by Group:" dropdown to display contacts belonging to that group.
Importing and Exporting Contacts
Export Contacts:

Navigate to File > Export Contacts.
Choose the destination and filename for the CSV file.
Import Contacts:

Navigate to File > Import Contacts.
Select the CSV file containing contacts to import.
Birthday Reminders
Upon startup, the application checks for contacts with birthdays today or within the next 7 days and displays a notification if any are found.
Project Structure
telephone-directory/
├── constants.py        # Contains constants like FILENAME and FIELDNAMES
├── data_manager.py     # Handles data operations (load, save, validate)
├── gui.py              # Defines the GUI of the application
├── main.py             # Entry point of the application
├── menu.py             # Defines the application's menu bar
├── utils.py            # Utility functions for input validation
└── contacts.csv        # CSV file storing contacts (auto-generated)
Additional Information
Data Validation: Ensures data integrity by validating inputs.
Date Format: Date of birth should be in DD.MM.YYYY format.
Encoding: UTF-8 encoding is used for proper character representation.
Possible Issues
Tkinter Not Installed: Install tkinter as per the Requirements.
Incorrect Character Display: Ensure your environment uses UTF-8 encoding.
File Permissions: Run the program with appropriate permissions to read/write files.
Planned Extensions
Favorites: Mark contacts as favorites for quick access.
Data Backup: Implement backup and restore functionalities.
Data Encryption: Encrypt contact data for enhanced security.
User Authentication: Add login system to protect access.
Contributing
Contributions are welcome! Please follow these steps:

Fork the Repository
Create a Feature Branch: git checkout -b feature/YourFeature
Commit Your Changes: git commit -am 'Add new feature'
Push to the Branch: git push origin feature/YourFeature
Open a Pull Request
Please ensure your code adheres to the project's coding standards and is well-documented.

License
This project is licensed under the MIT License.

Contact
If you have any questions, suggestions, or need assistance, feel free to reach out:

Email: ivanonenadicl@gmail.com
GitHub: ivo000
Thank you for using the Telephone Directory! Your feedback is highly appreciated.


---

**Note**:

- Remember to replace placeholders like `Your Name`, `your-username`, and `your.email@example.com` with your actual information.
- If you have screenshots or images, you can add them to the `Demo` section by uploading the images to your repository and linking them in the `README.md` file using the following Markdown syntax:

  ```markdown
  ## Demo

  ![Main Window](path/to/main_window.png)
You can also create a LICENSE file in your repository with the content of the MIT License or any other license you prefer.

If you have any badges (e.g., build status, license, etc.), you can add them at the top of the README.md file. For example:

# Telephone Directory 📞

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Make sure to include any other relevant information that might be helpful for users or contributors.

