def add_employee(employees):
    print("----Add new employee----")
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
    name=input("Enter name")
    department=input("Enter Department")
    role=input("Enter Role")
    while True:
        try:
            salary = int(input("Enter Salary: "))
            break  
        except ValueError:
    
            print("Invalid input. Please enter a number using only digits (0-9).")
    employee={
        "id":emp_id,
        "name":name,
        "department":department,
        "role":role,
        "salary":salary
    }
    employees.append(employee)

    print(f"Employee '{name}' added successfully!!")
