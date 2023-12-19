from employee import Employee
from employee_manager import EmployeeManager

def print_menu():
    print("\nMenu:")
    print("*" * 30)
    print("| {:<25} |".format("1. Display all employee data"))
    print("| {:<25} |".format("2. Add a new employee"))
    print("| {:<25} |".format("3. Remove an employee"))
    print("| {:<25} |".format("4. Update employee information"))
    print("| {:<25} |".format("0. Exit"))
    print("*" * 30)

def get_employee_choice(manager):
    manager.display_all_employees()
    choice = input("Select an employee (enter the number): ")
    return manager.get_employee_by_index(int(choice))

def main():
    file_path = "employees.json"
    manager = EmployeeManager(file_path)

    while True:
        print_menu()
        choice = input("Select an option: ")

        if choice == "1":
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
            employee_to_remove = get_employee_choice(manager)
            if employee_to_remove:
                manager.remove_employee(employee_to_remove)
                print(f"Employee {employee_to_remove.first_name} {employee_to_remove.last_name} successfully removed.")
            else:
                print("Invalid choice. Please select a valid employee.")
        elif choice == "4":
            employee_to_update = get_employee_choice(manager)
            if employee_to_update:
                first_name = input("Enter new first name: ")
                middle_name = input("Enter new middle name: ")
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email address: ")
                address = input("Enter new address: ")
                position = input("Enter new position: ")

                new_info = Employee(first_name, employee_to_update.last_name, middle_name,
                                    phone_number, email, address, position)
                manager.update_employee(employee_to_update, new_info)

                print(f"Information for employee {employee_to_update.first_name} {employee_to_update.last_name} "
                      f"successfully updated.")
            else:
                print("Invalid choice. Please select a valid employee.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please select a valid menu option.")

if __name__ == "__main__":
    main()
