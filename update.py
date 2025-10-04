def update_employee(employees):
    #Updates an employee, validating input using conditionals.
    print("\n--- Update Employee ---")
    # checks employees list is empty
    if not employees:
        print("No employees found. The list is empty.")
        return
    #Input employee Id and validate
    id_input = input("Enter the ID of the employee to update: ")
    if not id_input.isdigit():
        print("Invalid ID format. Please enter a number.")
        return
    #checks if employee Id is present in list or not
    emp_id = int(id_input)
    employee_to_update = None
    for emp in employees:
        if emp['id'] == emp_id:
            employee_to_update = emp
            break
    #If employee Id not exist
    if employee_to_update is None:
        print(f"Employee with ID {emp_id} not found.")
        return
    #if employee Id exists
    print("\nSelect the field to update:")
    print("1. Name\n2. Department\n3. Role\n4. Salary")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        employee_to_update['name'] = input("Enter new Name: ")
    elif choice == '2':
        employee_to_update['department'] = input("Enter new Department: ")
    elif choice == '3':
        employee_to_update['role'] = input("Enter new Role: ")
    elif choice == '4':
        while True:
            new_salary_input = input("Enter new Salary: ")
            try:
                # Try to convert the input to an integer
                new_salary = int(new_salary_input)
                # If successful, update the dictionary and exit the loop
                employee_to_update['salary'] = new_salary
                break
            except ValueError:
                # If the conversion fails, print an error and the loop will ask again
                print("Invalid input. Please enter numbers only.")
    else:
        print("Invalid choice. Returning to main menu.")
        return
    
    print(f"Employee details of '{employee_to_update['name']}' updated successfully!")