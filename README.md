# Library Management System

This is a command-line based Library Management System built with Python. It allows users (students, teachers, and admins) to manage books, user accounts, and borrowing/returning of books. The system uses a MySQL database to store all the information.

## Project Structure

The project is organized into several Python modules, each responsible for a specific functionality:

- `libmanagement.py`: The main application file that handles user login and menu navigation.
- `table creation.py`: Contains the SQL statements to create the necessary database tables. This script should be run once to set up the database.
- `addbook.py`: Adds new books to the library.
- `adview.py`: Provides book and user viewing options for the admin.
- `borrow.py`: Handles the borrowing of books by students and teachers.
- `returnbook.py`: Handles the returning of books and calculates fines for overdue books.
- `searchbook.py`: Allows users to search for books by name, author, or genre.
- `modify.py`: Allows the admin to modify book and user information.
- `lib_newaccount.py`: Creates new user accounts for students, teachers, and admins.
- `view.py`: Provides book viewing options for students and teachers.
- `requirements.txt`: Lists the required Python packages for this project.

## Setup Instructions

To run this project, you need to have Python and MySQL installed on your system.

### 1. Database Setup

1.  Make sure your MySQL server is running.
2.  Create a new database named `lms`. You can do this by running the following command in your MySQL client:
    ```sql
    CREATE DATABASE lms;
    ```
3.  The application connects to the database with the username `root` and password `Risa@1010`. You may need to update the `mycon` connection object in each `.py` file to match your MySQL credentials.

### 2. Install Dependencies

1.  It is recommended to use a virtual environment to manage the project's dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
2.  Install the required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Create Database Tables

Run the `table creation.py` script to create the necessary tables in the `lms` database:
```bash
python "table creation.py"
```

## Running the Application

To start the Library Management System, run the `libmanagement.py` script:
```bash
python libmanagement.py
```

This will launch the command-line interface, where you can log in as a student, teacher, or admin, or create a new account.
