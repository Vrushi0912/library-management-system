import result
import send
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3
import re

# Create a welcome message pop-up
messagebox.showinfo("Welcome!", "Welcome to the Library management system.")

# Create a function to handle the button click event
def create_database(event=None):

    try:
        # Get the database name from the user input
        db_name = db_name_entry.get()

        # Check if the database name is empty
        if not db_name:
            raise ValueError("Please enter a valid database name.")

        # Check if the database name is valid (starts with a letter and contains only letters, numbers, and underscores)
        if not re.match("^[a-zA-Z][a-zA-Z0-9_]*$", db_name):
            raise ValueError("Database name must start with a letter and can only contain letters, numbers, and underscores.")

        # Create a connection to the database
        conn = sqlite3.connect(str(db_name) + ".db")

        # Create a cursor object
        cursor = conn.cursor()

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Show a success message to the user
        messagebox.showinfo("Success", "The database " + str(db_name) + ".db has been created.")

    except Exception as e:
        # Show an error message to the user if something goes wrong
        messagebox.showerror("Error", "An error occurred: " + str(e))

# Create a tkinter frame
window = tk.Tk()
window.title("Library Managment Systeem")
window.configure(bg='Yellow')

frame = LabelFrame(window,padx=1,pady=1,bg='white')
frame.pack(padx=5,pady=5)

frame1 = LabelFrame(frame,padx=10,pady=10,bg='LightSkyBlue')
frame1.pack(padx=10,pady=10)

# Create a label for the database name input
db_name_label = tk.Label(frame1, text="Database Name:",bg='LightSkyBlue',fg='Black')
db_name_label.grid(row=0, column=0,ipadx=100)

# Create an entry field for the database name input
db_name_entry = tk.Entry(frame1)
db_name_entry.grid(row=0, column=1)

# Bind the <Return> event to the create_database function
db_name_entry.bind("<Return>", create_database)

# Create a button to create the database
create_db_button = tk.Button(frame1, text="Create Database", command=create_database)
create_db_button.grid(row=0, column=3, columnspan=2,padx=20, pady=10)

# Add a label for the table name input
table_name_label = tk.Label(frame1, text="Enter the name of the table:",bg='LightSkyBlue',fg='Black')
table_name_label.grid(row=2, column=0,ipadx=100)

# Create an entry field for the table name input
table_name_entry = tk.Entry(frame1)
table_name_entry.grid(row=2, column=1)

# Create labels for the column names
value_label = tk.Label(frame1, text="\nEnter table values (Click add after each value to add multiple values):\n",bg='LightSkyBlue',fg='Black')

studentid_label = tk.Label(frame1, text="StudentidID:",bg='LightSkyBlue',fg='Black')

bookname_label = tk.Label(frame1, text="BookName:",bg='LightSkyBlue',fg='Black')

class1_label = Label(frame1, text="Department:",bg='LightSkyBlue',fg='Black')

year_label = tk.Label(frame1, text="Year:",bg='LightSkyBlue',fg='Black')

issuedate_label = tk.Label(frame1, text="IssueDate:",bg='LightSkyBlue',fg='Black')

returndate_label = tk.Label(frame1, text="RteurnDate:",bg='LightSkyBlue',fg='Black')


#CREATE TABLE
def create_table():

    try:
        # Get the name of the table from the input field
        table_name = table_name_entry.get()

        # Create a connection to the database
        conn1 = sqlite3.connect(str(db_name_entry.get()) + ".db")

        # Create a cursor object
        cursor = conn1.cursor()

        # Create a table with the given name
        cursor.execute("CREATE TABLE IF NOT EXISTS " + str(table_name) + " (StuddetID INTEGER primary key AUTOINCREMENT, BookName TEXT,Class TEXT,Year TEXT,IssueDate TEXT,ReturnDate INTEGER)")

        # Commit the changes and close the connection
        conn1.commit()
        conn1.close()

        # Show a success message
        messagebox.showinfo("Success", "Table " + str(table_name) + " created successfully.")

    except Exception as e:
        # Show an error message if the table could not be created
        messagebox.showerror("Error", "An error occurred: " + str(e))

def insert_values():
    conn2 = sqlite3.connect(str(db_name_entry.get()) + ".db")

    # Get the table name and values from the entry widgets
    bookname = bookname_entry.get()
    class1 = class1_entry.get()
    year = year_var.get()
    issuedate = issuedate_entry.get()
    returndate =returndate_entry.get()

    # Check if the inputted values match the expected data types
    try:
        issuedate  = int(issuedate )
        returndate = float(returndate)
    except ValueError as err:
        messagebox.showerror("Error", "Invalid input: "+str(err))
        return

    # Construct the SQL query string
    sql_query = "INSERT INTO "+str(table_name_entry.get())+" VALUES (null,?,?,?,?,?)"

    # Clear the entry widgets
    bookname_entry.delete(0, tk.END)
    class1_entry.delete(0,tk.END)
    year_var.set("Select year")
    issuedate_entry.delete(0, tk.END)
    returndate_entry.delete(0, tk.END)

    # Create a cursor object
    cursor = conn2.cursor()

    # Execute the SQL query
    cursor.execute(sql_query, (bookname, class1, year, issuedate, returndate))
    conn2.commit()
    conn2.close()


# Create a button to create the table
create_table_button = tk.Button(frame1, text="Create Table", command=create_table)
create_table_button.grid(row=2, column=3, columnspan=2,padx=20, pady=10,ipadx=12)

# Add the column name labels to the frame1 using grid geometry manager
value_label.grid(row=5, column=0)

studentid_label.grid(row=7, column=0,pady=5,ipadx=12)

bookname_label.grid(row=8, column=0,pady=10)

class1_label.grid(row=9, column=0,pady=10)

year_label.grid(row=10, column=0,pady=10)

issuedate_label.grid(row=11, column=0,pady=10,ipadx=6)

returndate_label.grid(row=12, column=0,pady=10,ipadx=0)

# Create the entry and option menu widgets
studentid1_label = tk.Label(frame1,text = "AutoFill",bg='LightSkyBlue',fg='black')
studentid1_label.grid(row=7, column=1,pady=10,ipadx=50)

bookname_entry = tk.Entry(frame1)
bookname_entry.grid(row=8, column=1,pady=20,ipadx=50)

class1_entry = tk.Entry(frame1)
class1_entry.grid(row=9, column=1,pady=10,ipadx=50)

year_var = tk.StringVar()
year_var.set("Select Class")
year_option = tk.OptionMenu(frame1, year_var, "FY", "SY", "TY")
year_option.grid(row=10, column=1,pady=10,ipadx=15)


issuedate_entry = tk.Entry(frame1)
issuedate_entry.grid(row=11, column=1,pady=10,ipadx=50)

returndate_entry = tk.Entry(frame1)
returndate_entry.grid(row=12, column=1,pady=10,ipadx=50)

# Create the button to insert values into the user-defined table
insert_button = tk.Button(frame1, text="Submit", command=insert_values)
insert_button.grid(row=13, column=1,pady=10,ipadx=50)

#Clear button
def clear():
        db_name_entry.delete(0,tk.END)
        table_name_entry.delete(0,tk.END)
        bookame_entry.delete(0, tk.END)
        class1_entry.delete(0,tk.END)
        year_var.set("Select year")
        issuedate_entry.delete(0, tk.END)
        returndate_entry.delete(0, tk.END)
    
    
clear_button = tk.Button(frame1, text="Clear", command=clear)
clear_button.grid(row=12, column=5,ipadx=15,pady=18)

result_button = tk.Button(frame1, text="Save", command=result.resultbutton)
result_button.grid(row=13, column=4,ipadx=10)

result_button = tk.Button(frame1, text="Send", command=send.sendbutton)
result_button.grid(row=13, column=5,ipadx=15)

# Run the tkinter event loop
window.mainloop()
