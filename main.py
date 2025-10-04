from add import add_employee
from view import view_employees
from search import search_employee
from update import update_employee
from delete import delete_employee

def emp_management_sys():
    employees=[]
    while True:
        print("======Employee Management System======")
        print("1.Add Employee")
        print("2.View Employee")
        print("3.Search Employee")
        print("4.Update Employee")
        print("5.Delete Employee")
        print("6.Exit")

        choice=input("enter your choice(1-6):")
        if choice=='1':
            add_employee(employees)
        elif choice=='2':
            view_employees(employees)
        elif choice=='3':
            search_employee(employees)
        elif choice=='4':
            update_employee(employees)
        elif choice=='5':
            delete_employee(employees)
        elif choice=='6':
            print("Thank You!!!")
            break
        else:
            print("Invalid choice!Please enter correct choice between 1-6")


emp_management_sys()
        


