import socket
import sqlite3
import tkinter as tk
from tkinter import messagebox

def recv():
    # Define the host and port to listen on
    HOST = '0.0.0.0'
    PORT = 1234

    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    sock.bind((HOST, PORT))

    # Listen for incoming connections
    sock.listen(2)

    # Accept a connection
    conn, addr = sock.accept()

    # Receive the file contents from the sender
    file_contents = b''
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file_contents += data

    # Save the file contents to disk
    with open('result.db', 'wb') as f:
        f.write(file_contents)

    # Close the connection and the socket
    conn.close()
    sock.close()

    # Create a pop-up message
    root = tk.Tk()
    messagebox.showinfo('Database Received', 'The database has been received and connected as result.db')
    root.mainloop()

