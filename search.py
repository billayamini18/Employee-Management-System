def search_employee(employees):
    #Searches for the first employee matching a specific ID.
    print("Search employee by ID")
    if not employees:
        print("Employee list is empty")
        return
    search_id=input("Enter the id of employee to search:")
    # Loop through each employee in the list
    for emp in employees:
        # Compare the employee's ID (as a string) to the user's input
        if emp['id']==int(search_id):
            print("\n----Employee Found----")
            print(f"  ID: {emp['id']}")
            print(f"  Name: {emp['name']}")
            print(f"  Department: {emp['department']}")
            print(f"  Role: {emp['role']}")
            print(f"  Salary: ${emp['salary']}")
            return # Exit the function immediately after finding the employee
    # This line will only be reached if the loop finishes without finding a match
    print(f"\n Employee with ID '{search_id}' not found.")

