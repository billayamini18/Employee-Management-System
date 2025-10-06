def view_employees(employees):
    print("\n--- All Employees ---")
    if not employees:
        print("No employees found. The list is empty.")
        return
    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}, Role: {emp['role']}, Salary: ${emp['salary']}")    

    
