import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhavana@2242",
    database="EMPLOYEE_MANAGEMENT"
)

cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    department VARCHAR(100),
    designation VARCHAR(100),
    salary DECIMAL(10,2),
    phone VARCHAR(15),
    email VARCHAR(100)
)
"""

cursor.execute(create_table_query)

connection.commit()

print("Employee table created successfully!")

cursor.close()
connection.close()