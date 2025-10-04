def add_employee(employees):
    # Adds a new employee after validating input using conditionals.
    print("----Add new employee----")
    # Input and Validate Employee ID
    while True:
        id_input=input("Enter employee_id")
        if not id_input.isdigit():
            print("Invalid Employee Id.......Please enter correctly")
            continue
        emp_id = int(id_input)
        if any(emp['id']==emp_id for emp in employees):
            print("Employee id already exists. Please enter a different one.")
            continue
        else:
            break            
    # Input other details
    name=input("Enter name")
    department=input("Enter Department")
    role=input("Enter Role")
    while True:
        try:
            salary = int(input("Enter Salary: "))
            break  # This line is only reached if int() succeeds
        except ValueError:
            # This code runs if a ValueError occurs
            print("Invalid input. Please enter a number using only digits (0-9).")
    # Create the employee dictionary
    employee={
        "id":emp_id,
        "name":name,
        "department":department,
        "role":role,
        "salary":salary
    }
    #adds to employees
    employees.append(employee)
    print(f"Employee '{name}' added successfully!!")