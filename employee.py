from database import connect_db

def add_employee():
    connection = connect_db()
    cursor = connection.cursor()

    employee_id = int(input("Enter Employee ID: "))

    if employee_id <= 0:
        print("Employee ID must be greater than 0.")
        cursor.close()
        connection.close()
        return

    name = input("Enter Employee Name: ")
    age = int(input("Enter Age: "))

    if age < 18 or age > 60:
        print("Age must be between 18 and 60.")
        cursor.close()
        connection.close()
        return

    gender = input("Enter Gender: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))

    if salary < 0:
        print("Salary cannot be negative.")
        cursor.close()
        connection.close()
        return

    phone = input("Enter Phone Number: ")

    if len(phone) != 10 or not phone.isdigit():
        print("Invalid Phone Number! Please enter exactly 10 digits.")
        cursor.close()
        connection.close()
        return

    email = input("Enter Email: ")

    if "@" not in email or "." not in email:
        print("Invalid Email Address!")
        cursor.close()
        connection.close()
        return

    check_query = "SELECT * FROM employees WHERE employee_id = %s"

    cursor.execute(check_query, (employee_id,))

    existing_employee = cursor.fetchone()

    if existing_employee:
        print("Employee ID already exists.")
        cursor.close()
        connection.close()
        return
    
    query = """
    INSERT INTO employees
    (employee_id, name, age, gender, department, designation, salary, phone, email)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        employee_id,
        name,
        age,
        gender,
        department,
        designation,
        salary,
        phone,
        email
    )

    try:
        cursor.execute(query, values)
        connection.commit()
        print("\nEmployee Added Successfully!")

    except Exception as e:
        print("\nError:", e)

    finally:
        cursor.close()
        connection.close()

def view_employees():

    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM employees")

        employees = cursor.fetchall()

        if not employees:
            print("No Employees Found.")
            return

        print("\nEmployee Details\n")

        for emp in employees:
            print(f"""
Employee ID : {emp[0]}
Name        : {emp[1]}
Age         : {emp[2]}
Gender      : {emp[3]}
Department  : {emp[4]}
Designation : {emp[5]}
Salary      : {emp[6]}
Phone       : {emp[7]}
Email       : {emp[8]}
-----------------------------------
""")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()

def search_employee():

    connection = connect_db()
    cursor = connection.cursor()

    try:
        print("\nSearch Employee")
        print("1. Search by Employee ID")
        print("2. Search by Employee Name")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = int(input("Enter Employee ID: "))

            cursor.execute(
                "SELECT * FROM employees WHERE employee_id = %s",
                (emp_id,)
            )

        elif choice == "2":
            name = input("Enter Employee Name: ")

            cursor.execute(
                "SELECT * FROM employees WHERE name = %s",
                (name,)
            )

        else:
            print("Invalid Choice")
            return

        employee = cursor.fetchone()

        if employee:
            print(f"""
Employee ID : {employee[0]}
Name        : {employee[1]}
Age         : {employee[2]}
Gender      : {employee[3]}
Department  : {employee[4]}
Designation : {employee[5]}
Salary      : {employee[6]}
Phone       : {employee[7]}
Email       : {employee[8]}
""")
        else:
            print("Employee Not Found.")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()

def update_employee():

    connection = connect_db()
    cursor = connection.cursor()

    emp_id = int(input("Enter Employee ID: "))

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Gender")
    print("4. Department")
    print("5. Designation")
    print("6. Salary")
    print("7. Phone")
    print("8. Email")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":
            new_value = input("Enter New Name: ")
            query = "UPDATE employees SET name=%s WHERE employee_id=%s"

        elif choice == "2":
            new_value = int(input("Enter New Age: "))
            query = "UPDATE employees SET age=%s WHERE employee_id=%s"

        elif choice == "3":
            new_value = input("Enter New Gender: ")
            query = "UPDATE employees SET gender=%s WHERE employee_id=%s"

        elif choice == "4":
            new_value = input("Enter New Department: ")
            query = "UPDATE employees SET department=%s WHERE employee_id=%s"

        elif choice == "5":
            new_value = input("Enter New Designation: ")
            query = "UPDATE employees SET designation=%s WHERE employee_id=%s"

        elif choice == "6":
            new_value = float(input("Enter New Salary: "))
            query = "UPDATE employees SET salary=%s WHERE employee_id=%s"

        elif choice == "7":
            new_value = input("Enter New Phone Number: ")
            query = "UPDATE employees SET phone=%s WHERE employee_id=%s"

        elif choice == "8":
            new_value = input("Enter New Email: ")
            query = "UPDATE employees SET email=%s WHERE employee_id=%s"

        else:
            print("Invalid Choice")
            return

        cursor.execute(query, (new_value, emp_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Employee Updated Successfully!")
        else:
            print("Employee ID Not Found.")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()
    
def delete_employee():

    connection = connect_db()
    cursor = connection.cursor()

    emp_id = int(input("Enter Employee ID to Delete: "))

    confirm = input("Are you sure you want to delete this employee? (Y/N): ")

    if confirm.upper() != "Y":
        print("Delete operation cancelled.")
        cursor.close()
        connection.close()
        return

    query = """
    DELETE FROM employees
    WHERE employee_id = %s
    """

    try:
        cursor.execute(query, (emp_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Employee Deleted Successfully!")
        else:
            print("Employee Not Found.")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()
def employee_statistics():
    connection = connect_db()
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT COUNT(*) FROM employees")
        total = cursor.fetchone()[0]

        cursor.execute("SELECT MAX(salary) FROM employees")
        highest = cursor.fetchone()[0]

        cursor.execute("SELECT MIN(salary) FROM employees")
        lowest = cursor.fetchone()[0]

        cursor.execute("SELECT AVG(salary) FROM employees")
        average = cursor.fetchone()[0]

        print("\n==============================")
        print(" Employee Statistics")
        print("==============================")
        print(f"Total Employees : {total}")
        print(f"Highest Salary  : {highest}")
        print(f"Lowest Salary   : {lowest}")
        print(f"Average Salary  : {average:.2f}")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()