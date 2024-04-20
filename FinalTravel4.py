import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import sqlite3
import pandas as pd
from tkcalendar import DateEntry


# Database initialization
conn = sqlite3.connect('Travel__management.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS customers
        (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT,  hotel_name TEXT, room_type TEXT, num_adults INTEGER, num_children INTEGER,
         payment_method TEXT, checkin_date TEXT, checkout_date TEXT, num_days INTEGER,
         transportation_type TEXT, pickup_location TEXT, dropoff_location TEXT,notes TEXT)''')
# Added table for admin credentials-
c.execute('''CREATE TABLE IF NOT EXISTS admin_credentials
        (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
# Inserting default admin credentials
c.execute("INSERT OR IGNORE INTO admin_credentials (id, username, password) VALUES (1, 'Bodz', '_123')")
conn.commit()

# Functions
def admin_signin():
    def check_credentials():
        username = username_entry.get()
        password = password_entry.get()

        # Check if the entered credentials match the stored admin credentials
        c.execute("SELECT * FROM admin_credentials WHERE username=? AND password=?", (username, password))
        if c.fetchone():
            messagebox.showinfo("Success", "Admin Sign-in Successful")
            signin_window.destroy()
            root.withdraw()
            admin_panel()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    signin_window = tk.Toplevel(root)
    signin_window.title("Admin Sign-in")
    signin_window.configure(bg='darkslategray')
    signin_window.geometry('250x100')

    username_label = tk.Label(signin_window, text="Username", bg='gray10', fg='white')
    username_label.grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(signin_window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(signin_window, text="Password", bg='gray10', fg='white')
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(signin_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    signin_button = tk.Button(signin_window, text="Sign in", command=check_credentials, bg='gray10', fg='white')
    signin_button.grid(row=2, columnspan=2, padx=10, pady=5)


def admin_panel():
    def add_customer():
        def save():
            name = name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            num_adults = adults_spinbox.get()
            num_children = children_spinbox.get()
            payment_method = payment_method_var.get()
            checkin_date = checkin_date_entry.get()
            checkout_date = checkout_date_entry.get()
            num_days = num_days_entry.get()
            transportation_type = transport_type_var.get()
            pickup_location = pickup_entry.get()
            dropoff_location = dropoff_entry.get()
            hotel_name = hotel_name_ent.get()
            room_type = room_type_var.get()
            notes = notes_text.get("1.0", "end-1c")

            c.execute("INSERT INTO customers VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?,?, ?, ?)",
                      (name, phone, email, hotel_name, room_type, num_adults, num_children, payment_method,
                       checkin_date, checkout_date, num_days,
                       transportation_type, pickup_location, dropoff_location, notes))
            conn.commit()
            messagebox.showinfo('Success', 'Customer added successfully')
            top.destroy()
            root.withdraw()

        top = tk.Toplevel(root)
        top.title('Add Customer')
        top.configure(bg='darkslategray')
        name_label = tk.Label(top, text='Name', bg='gray10', fg='white')
        name_label.grid(row=1, column=0, pady=10)
        name_entry = tk.Entry(top)
        name_entry.grid(row=1, column=1, pady=10)

        phone_label = tk.Label(top, text='Phone', bg='gray10', fg='white')
        phone_label.grid(row=2, column=0, pady=10)
        phone_entry = tk.Entry(top)
        phone_entry.grid(row=2, column=1, pady=10)

        email_label = tk.Label(top, text='Email', bg='gray10', fg='white')
        email_label.grid(row=3, column=0, pady=10)
        email_entry = tk.Entry(top)
        email_entry.grid(row=3, column=1, pady=10)

        hotel_name = tk.Label(top, text='Hotel', bg='gray10', fg='white')
        hotel_name.grid(row=4, column=0, pady=10)
        hotel_name_ent = tk.Entry(top)
        hotel_name_ent.grid(row=4, column=1, pady=10)

        room_type = tk.Label(top, text='Room Type', bg='gray10', fg='white')
        room_type.grid(row=5, column=0, pady=10)
        room_type_var = tk.StringVar()
        room_type_var_mu = tk.OptionMenu(top, room_type_var, 'Single', 'Double', 'Triple')
        room_type_var_mu.grid(row=5, column=1, pady=10)

        adults_label = tk.Label(top, text='Number of Adults', bg='gray10', fg='white')
        adults_label.grid(row=6, column=0, pady=10)
        adults_spinbox = tk.Spinbox(top, from_=0, to=100)
        adults_spinbox.grid(row=6, column=1, pady=10)

        children_label = tk.Label(top, text='Number of Children', bg='gray10', fg='white')
        children_label.grid(row=7, column=0, pady=10)
        children_spinbox = tk.Spinbox(top, from_=0, to=100)
        children_spinbox.grid(row=7, column=1, pady=10)

        payment_method_label = tk.Label(top, text='Payment Method', bg='gray10', fg='white')
        payment_method_label.grid(row=8, column=0, pady=10)
        payment_method_var = tk.StringVar()
        payment_method_menu = tk.OptionMenu(top, payment_method_var, 'Credit Card', 'Debit card ', 'Cash', 'Bank Transfer', 'instapay', 'vodafone cash')
        payment_method_menu.grid(row=8, column=1, pady=10)

        checkin_date_label = tk.Label(top, text='Check-in Date', bg='gray10', fg='white')
        checkin_date_label.grid(row=9, column=0, pady=10)
        checkin_date_entry = DateEntry(top, date_pattern='yyyy-mm-dd')
        checkin_date_entry.grid(row=9, column=1, pady=10)

        checkout_date_label = tk.Label(top, text='Checkout Date', bg='gray10', fg='white')
        checkout_date_label.grid(row=10, column=0, pady=10)
        checkout_date_entry = DateEntry(top, date_pattern='yyyy-mm-dd')
        checkout_date_entry.grid(row=10, column=1, pady=10)

        num_days_label = tk.Label(top, text='Number of Days', bg='gray10', fg='white')
        num_days_label.grid(row=11, column=0, pady=10)
        num_days_entry = tk.Spinbox(top, from_=0, to=100)
        num_days_entry.grid(row=11, column=1, pady=10)

        transport_type_label = tk.Label(top, text='Transportation Type', bg='gray10', fg='white')
        transport_type_label.grid(row=12, column=0, pady=10)
        transport_type_var = tk.StringVar()
        transport_type_menu = tk.OptionMenu(top, transport_type_var, 'Private Car', 'Bus', 'Train', 'Plane')
        transport_type_menu.grid(row=12, column=1, pady=10)

        pickup_label = tk.Label(top, text='Pickup Location', bg='gray10', fg='white')
        pickup_label.grid(row=13, column=0, pady=10)
        pickup_entry = tk.Entry(top)
        pickup_entry.grid(row=13, column=1, pady=10)

        dropoff_label = tk.Label(top, text='Dropoff Location', bg='gray10', fg='white')
        dropoff_label.grid(row=14, column=0, pady=10)
        dropoff_entry = tk.Entry(top)
        dropoff_entry.grid(row=14, column=1, pady=10)

        notes_label = tk.Label(top, text='Notes', bg='gray10', fg='white')
        notes_label.grid(row=15, column=0, pady=10)
        notes_text = tk.Text(top, height=4, width=30)
        notes_text.grid(row=15, column=1, pady=10)

        save_button = tk.Button(top, text='Save', command=save, bg='gray10', fg='white')
        save_button.grid(row=16, column=0, pady=10)
        # top.destroy()
        root.withdraw()

    def view_customers():
        customers = c.execute('SELECT * FROM customers ')
        top = tk.Toplevel(root)
        top.title('View Customers')
        top.configure(bg='darkslategray')

        tree = ttk.Treeview(top)
        tree['columns'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15')
        tree.column('#0', width=0, stretch=tk.NO)
        tree.column('1', anchor=tk.N, width=100)
        tree.column('2', anchor=tk.N, width=100)
        tree.column('3', anchor=tk.N, width=100)
        tree.column('4', anchor=tk.N, width=100)
        tree.column('5', anchor=tk.N, width=100)
        tree.column('6', anchor=tk.N, width=100)
        tree.column('7', anchor=tk.N, width=100)
        tree.column('8', anchor=tk.N, width=100)
        tree.column('9', anchor=tk.N, width=100)
        tree.column('10', anchor=tk.N, width=100)
        tree.column('11', anchor=tk.N, width=150)
        tree.column('12', anchor=tk.N, width=150)
        tree.column('13', anchor=tk.N, width=150)
        tree.column('14', anchor=tk.N, width=150)
        tree.column('15', anchor=tk.N, width=150)
        tree.heading('1', text='Name')
        tree.heading('2', text='Phone')
        tree.heading('3', text='Email')
        tree.heading('4', text='Hotel')
        tree.heading('5', text='Room type')
        tree.heading('6', text='Adults')
        tree.heading('7', text='Childrens')
        tree.heading('8', text='Payment Method')
        tree.heading('9', text='Check-in Date')
        tree.heading('10', text='Checkout Date')
        tree.heading('11', text='Number of Days')
        tree.heading('12', text='Transport Type')
        tree.heading('13', text='Pickup Location')
        tree.heading('14', text='Drop off Location')
        tree.heading('15', text='Notes')

        for customer in customers:
            tree.insert('', 'end', text=customer[0], values=customer[1:])
        tree.pack(expand=True, fill='both')

    admin_panel_window = tk.Toplevel(root)
    admin_panel_window.title("Admin Screen")
    admin_panel_window.geometry("300x150")
    admin_panel_window.configure(bg='darkslategray')

    add_customer_button = tk.Button(admin_panel_window, text="Add Customer", command=add_customer)
    add_customer_button.pack(pady=10)

    view_customers_button = tk.Button(admin_panel_window, text="View Customers", command=view_customers)
    view_customers_button.pack(pady=10)

    save_to_excel_button = tk.Button(admin_panel_window, text='Save to Excel', command=save_to_excel)
    save_to_excel_button.pack(pady=10)



def about_fun():
    about_panel_window = tk.Tk()
    about_panel_window.title("About Application")
    about_panel_window.geometry("300x150")
    about_panel_window.configure(bg='darkslategray')


    text_widget = tk.Text(about_panel_window, bg="white", fg="black", bd=2, height=10, width=40,font="Arial")


    # Inserting some text into the widget
    text_widget.insert(tk.END, "This program is Created by Bodz.")

    # Pack the Text widget to make it visible
    text_widget.pack()


def save_to_excel():
    customers = c.execute('SELECT * FROM customers')
    data = [customer for customer in customers]
    df = pd.DataFrame(data, columns=['ID', 'Name', 'Phone', 'Email', 'Hotel', 'Room_type', 'Adults', 'Childrens', 'Payment Method',
                                         'Check-in Date', 'Checkout Date', 'Number of Days', 'Transport Type',
                                         'Pickup Location', 'Dropoff Location', 'Notes'])
    file_path = tk.filedialog.asksaveasfilename(defaultextension='.xlsx',
                                                    filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df.to_excel(file_path, index=False)
        messagebox.showinfo('Success', 'Customer data saved to Excel file.')




# Main window
root = tk.Tk()
root.title("Bodz Travel Company")
root.geometry("375x200")
root.configure(bg='darkslategray')



image = Image.open("Bt.png")
aspect_ratio = image.width / image.height
target_height = 250
target_width = int(target_height * aspect_ratio)
image = image.resize((target_width, target_height))
bg_image = ImageTk.PhotoImage(image)
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()
canvas.create_image(0, 0, image=bg_image, anchor="nw")


#bottom_frame = tk.Frame(root, bg="lightblue")  # Set the background color here
#bottom_frame.pack(side="bottom", fill="x")

signin_button = tk.Button(root, text="Admin Sign-in", command=admin_signin)
signin_button.place(relx=0.5, rely=0.40, anchor="center")

about_button = tk.Button(root, text="About", command=about_fun)
about_button.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
# Close the database connection when the application exits
conn.close()
