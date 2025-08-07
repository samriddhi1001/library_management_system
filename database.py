import mysql.connector as ctr

def get_connection():
    """
    Establishes a connection to the MySQL database and returns the connection and cursor objects.
    """
    mycon = ctr.connect(host="localhost", user="root", password="Risa@1010", database="lms")
    if not mycon.is_connected():
        print("Not connected")
    mycur = mycon.cursor()
    return mycon, mycur
