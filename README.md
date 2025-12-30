# Library Management System

A robust and user-friendly desktop application for managing library operations and result processing, built with Python and Tkinter.

## 📋 Overview

The Library Management System is designed to streamline the day-to-day activities of a library. It allows administrators to create and manage databases, handle student records, track book issues and returns, and even transfer data between systems using socket programming. This application simplifies record-keeping and ensures data integrity with a local SQLite database.

## ✨ Key Features

-   **Database Management**: Easily create new SQLite databases and tables directly from the UI.
-   **Student & Book Tracking**: Manage student IDs, book names, departments, years, create and manage records.
-   **Issue & Return System**: Track issue dates and return dates for books.
-   **Data Transfer**: Integrated file sender and receiver modules to transfer database files between computers over a network.
-   **User-Friendly Interface**: Intuitive GUI built with Tkinter for easy navigation.
-   **Data Validation**: Built-in checks to ensure valid data entry (e.g., date formats, numeric fields).

## 🛠️ Tech Stack

-   **Language**: Python 3
-   **GUI Framework**: Tkinter
-   **Database**: SQLite3
-   **Networking**: Python `socket` module
-   **OS**: Windows / Linux / macOS

## 📂 Project Structure

```
├── result_creation.py   # Main application entry point for database/table creation
├── result.py           # Logic for handling results/saving data
├── send.py             # Module for sending files/data over network
├── recv.py             # Module for receiving files/data
├── result_display.py   # Display logic for query results
└── README.md           # Project documentation
```

## 🚀 Getting Started

### Prerequisites

-   Python 3.x installed on your system.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/library-management-system.git
    cd library-management-system
    ```

2.  Install dependencies (Standard libraries used, no external pip install required usually, but ensure Tkinter is installed):
    ```bash
    # Tkinter is usually included with Python. If not:
    # On Ubuntu/Debian: sudo apt-get install python3-tk
    ```

### Running the Application

1.  To start the main management interface:
    ```bash
    python result_creation.py
    ```

2.  To use the file transfer feature, run the receiver on the destination machine first:
    ```bash
    python recv.py
    ```
    And the sender logic is integrated into the main app or call:
    ```bash
    python send.py
    ```

## 🔮 Future Enhancements

-   Authentication system for librarians.
-   Barcode scanning integration for books.
-   Export reports to CSV/PDF.
-   Modern UI overhaul with `customtkinter`.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✍️ Author

Developed by [Your Name]
