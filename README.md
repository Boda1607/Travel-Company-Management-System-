# Travel-Company-Management-System-
Project Overview:
The provided code is for a travel management system application built using Tkinter, a Python GUI library. It allows users to manage customer bookings, view customer data, and export customer data to an Excel file. The application has two main functionalities: customer management and admin authentication.
[9:39 PM]
Features:
Admin Sign-in:
Allows admins to sign in with a username and password.
Upon successful authentication, grants access to the admin panel.
Admin Panel:
Add Customer: Allows admins to add new customer details including name, contact information, booking details (hotel, room type, etc.), and transportation details.
View Customers: Displays a list of all customers along with their details in a tabular format.
Save to Excel: Enables admins to export customer data to an Excel file.
About:
Displays information about the application and its creator.
Database Integration:
The application utilizes SQLite for database management.
Two tables are created in the database: customers to store customer information and admin_credentials to store admin login credentials.
GUI Design:
The GUI is designed using Tkinter widgets and components.
Each functionality (admin sign-in, admin panel, about) is associated with buttons that trigger the respective actions.
Input fields, dropdown menus, spinboxes, and text areas are provided for capturing customer details.
Additional Libraries:
The code uses additional libraries such as PIL (Python Imaging Library) for image manipulation, pandas for data manipulation, and tkcalendar for date selection.
Workflow:
Upon running the application, users are presented with options to sign in as an admin or view information about the application.
Admins can sign in using their credentials and access the admin panel.
In the admin panel, admins can add new customers, view existing customer data, and export customer data to an Excel file.
The "About" section provides information about the application and its creator.
Next Steps:
Further enhancements could include user authentication for customer access, improved GUI design, additional functionalities such as editing and deleting customer records, and error handling mechanisms.
