def search_employee(employees):
    print("Search employee by ID")
    if not employees:
        print("Employee list is empty")
        return
    search_id=input("Enter the id of employee to search:")
    for emp in employees:
        if emp['id']==int(search_id):
            print("\n----Employee Found----")
            print(f"  ID: {emp['id']}")
            print(f"  Name: {emp['name']}")
            print(f"  Department: {emp['department']}")
            print(f"  Role: {emp['role']}")
            print(f"  Salary: ${emp['salary']}")
            return
    print(f"\n Employee with ID '{search_id}' not found.")


