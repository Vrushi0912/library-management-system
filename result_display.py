import recv
import tkinter as tk
import sqlite3
from tkinter import messagebox


# Create a tkinter window
window = tk.Tk()
window.title("History")
window.configure(bg='Yellow')

# Create a frame to hold the widgets
frame = tk.Frame(window,padx=1,pady=1,bg='white')
frame.pack(padx=5,pady=5)
frame1 = tk.Frame(frame,padx=10,pady=10,bg='LightSkyBlue')
frame1.pack(padx=10,pady=10)

# Create a label and an entry box to input the table name
table_name_label = tk.Label(frame1, text="Table Name:", bg="LightSkyblue", fg="Black")
table_name_label.grid(row=1, column=0)
table_name_entry = tk.Entry(frame1)
table_name_entry.grid(row=1, column=1)

# Get the table name from the input widget
table_name = table_name_entry.get()


# Define a function to retrieve and display the results
def display_results():
    # Clear the display
    result_display.delete('1.0', tk.END)

    # Retrieve the results from the database
    conn = sqlite3.connect("result.db")
    c = conn.cursor()
    c.execute("SELECT * FROM " + table_name_entry.get())
    results = c.fetchall()
    result_text = "| StudentID |  BookName   |   Department   | Year | IssueDate |  ReturnDate |\n"
    result_display.insert(tk.END, result_text)
    # Display the results in the text box
    for row in results:
        result_text1 ="|  " + str(row[0]) + " |  " + str(row[1]) + "  |       " + str(row[2]) + "       |  " + str(row[3]) + "  |    " + str(row[4]) + "    |   " + str(row[5]) + "   | \n"
        result_display.insert(tk.END, result_text1)
 
# Define a function to delete a record from the database
def delete_record():
    try:
        sql_delete_query = "DELETE FROM " + table_name_entry.get() + " WHERE id = ? "
        c.execute(sql_delete_query, (record_id_entry.get(),))
        conn.commit()

        # Display a success message
        messagebox.showinfo("Record Deleted", "Record with StudetID " + str(record_studentid_entry.get()) + " deleted successfully from " + table_bookname_entry.get()+ " in " + db_name_entry.get() + " Click Display Result to see changes. ")

    except sqlite3.Error as error:
        # Display an error message if there was a problem deleting the record
        messagebox.showerror("Error", "Failed to delete record from " + str(table_name_entry.get()) + " in " + str(db_name_entry.get()) + ": " + str(error))



# Create a label and an entry box to input the database name
recv_label = tk.Label(frame1, text="Receive Database:", bg="LightSkyblue", fg="Black")
recv_label.grid(row=0, column=0)

# Create a button to connect to the database
connect_button = tk.Button(frame1, text="Receive and connect to database", command=recv.recv)
connect_button.grid(row=0, column=1,pady=5)

# Create a label and an entry box to input the table name
table_name_label = tk.Label(frame1, text="Table Name:", bg="LightSkyblue", fg="Black")
table_name_label.grid(row=1, column=0)
table_name_entry = tk.Entry(frame1)
table_name_entry.grid(row=1, column=1)

# Create a button to display the results
display_button = tk.Button(frame1, text="Display Results", command=display_results)
display_button.grid(row=1, column=3,pady=5)

# Create a label and a text box to display the results
result_label = tk.Label(frame1, text="Save:", bg="LightSkyblue", fg="Black")
result_label.grid(row=2, column=0)
result_display = tk.Text(frame1, height=15, width=70)
result_display.grid(row=3, column=1, columnspan=3)


break_label = tk.Label(frame1, text="------------------------------------", bg="LightSkyblue", fg="Black")
break_label.grid(row=4,column=0)
break2_label = tk.Label(frame1, text="------------------------------------", bg="LightSkyblue", fg="Black")
break2_label.grid(row=4,column=1)
break3_label = tk.Label(frame1, text="------------------------------------", bg="LightSkyblue", fg="Black")
break3_label.grid(row=4,column=2)
break4_label = tk.Label(frame1, text="------------------------------------", bg="LightSkyblue", fg="Black")
break4_label.grid(row=4,column=3)

delete_label = tk.Label(frame1, text="Delete data via ID:", bg="LightSkyblue", fg="Black")
delete_label.grid(row=5,column=0)

# Create a label and an entry box to input the record ID
record_id_label = tk.Label(frame1, text="Record ID:", bg="LightSkyblue", fg="Black")
record_id_label.grid(row=6, column=0,pady=5)
record_id_entry = tk.Entry(frame1)
record_id_entry.grid(row=6, column=1,pady=5)

# Create a button to delete the record
delete_button = tk.Button(frame1, text="Delete Record", command=delete_record)
delete_button.grid(row=6, column=3)

# Run the tkinter event loop
window.mainloop()

