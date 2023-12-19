from employee import Employee
from employee_manager import EmployeeManager

def print_menu():
    print("\nMenu:")
    print("1. Display all employee data")
    print("2. Add a new employee")
    print("3. Remove an employee")
    print("4. Update employee information")
    print("0. Exit")

def main():
    file_path = "employees.csv"
    manager = EmployeeManager(file_path)

    while True:
        print_menu()
        choice = input("Select an option: ")

        if choice == "1":
            print("\nAll employees:")
            manager.display_all_employees()
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            middle_name = input("Enter middle name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            position = input("Enter position: ")

            new_employee = Employee(first_name, last_name, middle_name, phone_number, email, address, position)
            manager.add_employee(new_employee)

            print("Employee successfully added.")
        elif choice == "3":
            last_name = input("Enter the last name of the employee you want to remove: ")
            for employee in manager.employees:
                if employee.last_name == last_name:
                    manager.remove_employee(employee)
                    print(f"Employee {last_name} successfully removed.")
                    break
            else:
                print(f"Employee with last name {last_name} not found.")
        elif choice == "4":
            last_name = input("Enter the last name of the employee whose information you want to update: ")
            for employee in manager.employees:
                if employee.last_name == last_name:
                    first_name = input("Enter new first name: ")
                    middle_name = input("Enter new middle name: ")
                    phone_number = input("Enter new phone number: ")
                    email = input("Enter new email address: ")
                    address = input("Enter new address: ")
                    position = input("Enter new position: ")

                    new_info = Employee(first_name, last_name, middle_name, phone_number, email, address, position)
                    manager.update_employee(employee, new_info)

                    print(f"Information for employee {last_name} successfully updated.")
                    break
            else:
                print(f"Employee with last name {last_name} not found.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please select a valid menu option.")

if __name__ == "__main__":
    main()
