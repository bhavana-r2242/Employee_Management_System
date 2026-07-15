import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bhavana@2242",
        database="EMPLOYEE_MANAGEMENT"
    )
    return connection

if __name__ == "__main__":
    connection = connect_db()

    if connection.is_connected():
        print("Connected to MySQL Successfully!")

    connection.close()