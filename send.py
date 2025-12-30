import socket
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def sendbutton():
    def send_file():
        # Get the IP address and file path from the GUI inputs
        ip_address = ip_entry.get()
        file_path = file_entry.get()
        
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Define the port of the receiver
        PORT = 1234
        
        # Connect to the receiver
        sock.connect((ip_address, PORT))

        # Open the file and read its contents
        with open(file_path, 'rb') as f:
            file_contents = f.read()

        # Send the file contents to the receiver
        sock.sendall(file_contents)

        # Close the socket
        sock.close()

        # Display a success message
        messagebox.showinfo('Database Sent', 'The database has been sent successfully!')

    def choose_file():
        # Open a file dialog to allow the user to choose a file
        file_path = filedialog.askopenfilename()
        
        # Update the file entry field with the chosen file path
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

    # Create the GUI window
    window = tk.Tk()
    window.title("File Sender")
    window.configure(bg="LightSkyBlue")

    frame = LabelFrame(window,padx=1,pady=1,bg='white')
    frame.pack(padx=5,pady=5)

    frame1 = LabelFrame(frame,padx=10,pady=10,bg='black')
    frame1.pack(padx=10,pady=10)

    # Create the IP address entry field
    ip_label = tk.Label(frame1, text="Receiver IP address:",bg="LightSkyBlue",fg="Black")
    ip_label.grid(row=0,column=0)
    ip_entry = tk.Entry(frame1)
    ip_entry.grid(row=0,column=1,pady=5)

    # Create the file entry field and "Choose File" button
    file_label = tk.Label(frame1, text="File to send:",bg="LightSkyBlue",fg="Black")
    file_label.grid(row=1,column=0)
    file_entry = tk.Entry(frame1)
    file_entry.grid(row=1,column=1,ipady=5,pady=5)
    choose_button = tk.Button(frame1, text="Choose File", command=choose_file)
    choose_button.grid(row=1,column=3,padx=5)

    # Create the "Send File" button and status label
    send_button = tk.Button(frame1, text="Send File", command=send_file)
    send_button.grid(row=2,column=1)

    # Start the GUI event loop
    window.mainloop()
