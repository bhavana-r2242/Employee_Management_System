from employee import (
    add_employee,
    view_employees,
    search_employee,
    update_employee,
    delete_employee,
    employee_statistics
)
while True:

    print("""
====================================
     Employee Management System
====================================

1. Add Employee
2. View Employees
3. Search Employee
4. update Employee
5. Delete Employee
6. Employee Statistics
7. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        employee_statistics()

    elif choice == "7":
        print("Thank You!")
        break