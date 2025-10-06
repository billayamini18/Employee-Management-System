def delete_employee(employees):
    print("----Delete employee----")
    if not employees:
        print("No employees found....list is empty!")
    id_input=input("Enter the employee_id that you want to delete")
    if not id_input.isdigit():
        print("Invalid input enter correctly")
        return

    emp_id=int(id_input)
    emp_to_delete=None
    for emp in employees:
        if emp['id']==emp_id:
            emp_to_delete=emp
            break
    if emp_to_delete is None:
        print("Employee to delete is not found")
    else:
        confirm=input(f"Are you sure you want to delete {emp_to_delete['name']}? (y/n): ")
        if confirm=='y':
            employees.remove(emp_to_delete)
            print(f"Employee '{emp_to_delete['name']}' deleted successfully")
        else:

            print("Deletion cancelled")
