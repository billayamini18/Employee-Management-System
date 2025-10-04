def delete_employee(employees):
    # Deletes an employee, validating the ID with a conditional.
    print("----Delete employee----")
    #if employees list is empty
    if not employees:
        print("No employees found....list is empty!")
    id_input=input("Enter the employee_id that you want to delete")
    #emp_id is not entered correctly
    if not id_input.isdigit():
        print("Invalid input enter correctly")
        return

    emp_id=int(id_input)
    emp_to_delete=None
    # Checks wheather employee id is present or not
    for emp in employees:
        if emp['id']==emp_id:
            emp_to_delete=emp
            break
    # If employee id not found
    if emp_to_delete is None:
        print("Employee to delete is not found")
    # If employee id is found
    else:
        confirm=input(f"Are you sure you want to delete {emp_to_delete['name']}? (y/n): ")
        if confirm=='y':
            employees.remove(emp_to_delete)
            print(f"Employee '{emp_to_delete['name']}' deleted successfully")
        else:
            print("Deletion cancelled")