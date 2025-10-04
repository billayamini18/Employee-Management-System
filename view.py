def view_employees(employees):
    # Displays all employee records as a numbered list.
    print("\n--- All Employees ---")
    if not employees:
        print("No employees found. The list is empty.")
        return
    # Loop through the list with an automatic counter starting from 1
    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}, Role: {emp['role']}, Salary: ${emp['salary']}")    
    print() # Adds a blank line at the end for spacing