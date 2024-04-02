import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Peterguchman@101",
        database="Reminder_System"
    )
    cursor = db_connection.cursor()

    # Check if username and password exist in the database
    query = "SELECT * FROM users WHERE User_Name = %s AND User_Password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        open_home_page(username)
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

    cursor.close()
    db_connection.close()

def open_signup_window():
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up Page")

    # Create and place widgets for sign up page
    signup_frame = tk.Frame(signup_window, padx=10, pady=10)
    signup_frame.pack()

    username_label = tk.Label(signup_frame, text="Username:")
    username_label.grid(row=0, column=0, sticky="w")
    username_entry_signup = tk.Entry(signup_frame)
    username_entry_signup.grid(row=0, column=1)

    password_label = tk.Label(signup_frame, text="Password:")
    password_label.grid(row=1, column=0, sticky="w")
    password_entry_signup = tk.Entry(signup_frame, show="*")
    password_entry_signup.grid(row=1, column=1)

    email_label = tk.Label(signup_frame, text="Email:")
    email_label.grid(row=2, column=0, sticky="w")
    email_entry = tk.Entry(signup_frame)
    email_entry.grid(row=2, column=1)

    phone_label = tk.Label(signup_frame, text="Phone:")
    phone_label.grid(row=3, column=0, sticky="w")
    phone_entry = tk.Entry(signup_frame)
    phone_entry.grid(row=3, column=1)

    position_label = tk.Label(signup_frame, text="Position:")
    position_label.grid(row=4, column=0, sticky="w")
    position_entry = tk.Entry(signup_frame)
    position_entry.grid(row=4, column=1)

    course_label = tk.Label(signup_frame, text="Course:")
    course_label.grid(row=5, column=0, sticky="w")
    course_entry = tk.Entry(signup_frame)
    course_entry.grid(row=5, column=1)

    year_label = tk.Label(signup_frame, text="Year of Study:")
    year_label.grid(row=6, column=0, sticky="w")
    year_entry = tk.Entry(signup_frame)
    year_entry.grid(row=6, column=1)

    submit_button = tk.Button(signup_frame, text="Submit", command=lambda: upload_data(
        username_entry_signup.get(), password_entry_signup.get(), email_entry.get(),
        phone_entry.get(), position_entry.get(), course_entry.get(), year_entry.get()))
    submit_button.grid(row=7, column=0, pady=5)

    back_button = tk.Button(signup_frame, text="Back", command=signup_window.destroy)
    back_button.grid(row=7, column=1, pady=5)

def upload_data(username, password, email, phone, position, course, year):
    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    cursor = db_connection.cursor()

    # Insert user data into database
    query = "INSERT INTO users (User_Name, User_Password, User_Email, User_Phone_Number, User_Role, Course, User_Year) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (username, password, email, phone, position, course, year))
    db_connection.commit()

    cursor.close()
    db_connection.close()

    messagebox.showinfo("Data Uploaded", "Data uploaded successfully!")

def open_home_page(username):
    home_page = tk.Toplevel(root)
    home_page.title("Home Page")

    # Create and place widgets for home page
    home_frame = tk.Frame(home_page, padx=10, pady=10)
    home_frame.pack()

    welcome_label = tk.Label(home_frame, text="Welcome " + username + "!")
    welcome_label.grid(row=0, column=0, columnspan=2)

    timetable_button = tk.Button(home_frame, text="Timetable", command=lambda: open_timetable(username))
    timetable_button.grid(row=1, column=0, pady=5)

    info_button = tk.Button(home_frame, text="Info", command=lambda: display_user_info(username))
    info_button.grid(row=1, column=1, pady=5)

    back_button = tk.Button(home_frame, text="Back", command=home_page.destroy)
    back_button.grid(row=2, columnspan=2, pady=5)

def display_user_info(username):
    info_window = tk.Toplevel(root)
    info_window.title("User Info")

    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Peterguchman@101",
        database="Reminder_System"
    )
    cursor = db_connection.cursor()

    # Retrieve user info from database
    query = "SELECT * FROM users WHERE User_Name = %s"
    cursor.execute(query, (username,))
    user_info = cursor.fetchone()

    # Create and place widgets for user info page
    tree = ttk.Treeview(info_window)
    tree["columns"] = ("User_Name", "User_Password", "User_Email", "User_Phone_Number", "User_Role", "Course", "User_Year")
    tree.heading("#0", text="User ID")
    tree.heading("User_Name", text="Username")
    tree.heading("User_Password", text="Password")
    tree.heading("User_Email", text="Email")
    tree.heading("User_Phone_Number", text="Phone")
    tree.heading("User_Role", text="Position")
    tree.heading("Course", text="Course")
    tree.heading("User_Year", text="Year")

    tree.insert("", tk.END, text=user_info[0], values=(user_info[1], user_info[2], user_info[3], user_info[4], user_info[5], user_info[6], user_info[7]))
    tree.pack()

    # Buttons for edit and delete
    edit_button = tk.Button(info_window, text="Edit", command=lambda: edit_user_info(user_info[0]))
    edit_button.pack(pady=5)

    delete_button = tk.Button(info_window, text="Delete", command=lambda: delete_user(user_info[0], info_window))
    delete_button.pack(pady=5)

    back_button = tk.Button(info_window, text="Back", command=info_window.destroy)
    back_button.pack(pady=5)

    cursor.close()
    db_connection.close()

def edit_user_info(user_id):
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit User Info")

    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Peterguchman@101",
        database="Reminder_System"
    )
    cursor = db_connection.cursor()

    # Retrieve user info from database
    query = "SELECT * FROM users WHERE User_ID = %s"
    cursor.execute(query, (user_id,))
    user_info = cursor.fetchone()

    # Create and place widgets for edit user info page
    edit_frame = tk.Frame(edit_window, padx=10, pady=10)
    edit_frame.pack()

    new_username_label = tk.Label(edit_frame, text="New Username:")
    new_username_label.grid(row=0, column=0, sticky="w")
    new_username_entry = tk.Entry(edit_frame)
    new_username_entry.insert(0, user_info[1])
    new_username_entry.grid(row=0, column=1)

    new_password_label = tk.Label(edit_frame, text="New Password:")
    new_password_label.grid(row=1, column=0, sticky="w")
    new_password_entry = tk.Entry(edit_frame, show="*")
    new_password_entry.insert(0, user_info[2])
    new_password_entry.grid(row=1, column=1)

    new_email_label = tk.Label(edit_frame, text="New Email:")
    new_email_label.grid(row=2, column=0, sticky="w")
    new_email_entry = tk.Entry(edit_frame)
    new_email_entry.insert(0, user_info[3])
    new_email_entry.grid(row=2, column=1)

    new_phone_label = tk.Label(edit_frame, text="New Phone:")
    new_phone_label.grid(row=3, column=0, sticky="w")
    new_phone_entry = tk.Entry(edit_frame)
    new_phone_entry.insert(0, user_info[4])
    new_phone_entry.grid(row=3, column=1)

    new_position_label = tk.Label(edit_frame, text="New Position:")
    new_position_label.grid(row=4, column=0, sticky="w")
    new_position_entry = tk.Entry(edit_frame)
    new_position_entry.insert(0, user_info[5])
    new_position_entry.grid(row=4, column=1)

    new_course_label = tk.Label(edit_frame, text="New Course:")
    new_course_label.grid(row=5, column=0, sticky="w")
    new_course_entry = tk.Entry(edit_frame)
    new_course_entry.insert(0, user_info[6])
    new_course_entry.grid(row=5, column=1)

    new_year_label = tk.Label(edit_frame, text="New Year of Study:")
    new_year_label.grid(row=6, column=0, sticky="w")
    new_year_entry = tk.Entry(edit_frame)
    new_year_entry.insert(0, user_info[7])
    new_year_entry.grid(row=6, column=1)

    update_button = tk.Button(edit_frame, text="Update", command=lambda: update_user_data(
        user_id, new_username_entry.get(), new_password_entry.get(), new_email_entry.get(),
        new_phone_entry.get(), new_position_entry.get(), new_course_entry.get(), new_year_entry.get(), edit_window))
    update_button.grid(row=7, columnspan=2, pady=5)

    back_button = tk.Button(edit_frame, text="Back", command=edit_window.destroy)
    back_button.grid(row=8, columnspan=2, pady=5)

    cursor.close()
    db_connection.close()


def update_user_data(user_id, username, password, email, phone, position, course, year, window):
    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Peterguchman@101",
        database="Reminder_System"
    )
    cursor = db_connection.cursor()

    # Update user data in the database
    query = "UPDATE users SET User_Name = %s, User_Password = %s, User_Email = %s, User_Phone_Number = %s, User_Role = %s, Course = %s, User_Year = %s WHERE User_ID = %s"
    cursor.execute(query, (username, password, email, phone, position, course, year, user_id))
    db_connection.commit()

    cursor.close()
    db_connection.close()

    messagebox.showinfo("Data Updated", "User data updated successfully!")
    window.destroy()


def delete_user(user_id, window):
    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Peterguchman@101",
        database="Reminder_System"
    )
    cursor = db_connection.cursor()

    # Delete user from the database
    query = "DELETE FROM users WHERE User_ID = %s"
    cursor.execute(query, (user_id,))
    db_connection.commit()

    cursor.close()
    db_connection.close()

    messagebox.showinfo("User Deleted", "User deleted successfully!")
    window.destroy()

def open_timetable(username):
    timetable_window = tk.Toplevel(root)
    timetable_window.title("Timetable")

    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Peterguchman@101",
        database="Reminder_System"
    )
    cursor = db_connection.cursor()

    # Retrieve timetable data from database
    query = "SELECT * FROM timetable WHERE Year_ID = (SELECT Year_ID FROM users WHERE User_Name = %s)"
    cursor.execute(query, (username,))
    timetable_data = cursor.fetchall()

    # Create and place widgets for timetable page
    tree = ttk.Treeview(timetable_window)
    tree["columns"] = ("Lesson_Name", "Lecturer", "Location", "Lesson_Time", "Lesson_Day")
    tree.heading("#0", text="ID")
    tree.heading("Lesson_Name", text="Lesson")
    tree.heading("Lecturer", text="Lecturer")
    tree.heading("Location", text="Location")
    tree.heading("Lesson_Time", text="Time")
    tree.heading("Lesson_Day", text="Day")


    for row in timetable_data:
        tree.insert("", tk.END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6]))
    tree.pack()

    back_button = tk.Button(timetable_window, text="Back", command=timetable_window.destroy)
    back_button.pack()

    cursor.close()
    db_connection.close()

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create and place widgets for login page
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

username_label = tk.Label(frame, text="Username:")
username_label.grid(row=0, column=0, sticky="w")
username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(frame, text="Password:")
password_label.grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(frame, text="Login", command=login)
login_button.grid(row=2, column=0, pady=5)

signup_button = tk.Button(frame, text="Signup", command=open_signup_window)
signup_button.grid(row=2, column=1, pady=5)

# Run the application
root.mainloop()
