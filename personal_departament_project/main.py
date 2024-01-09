from employee import Employee
from employee_manager import EmployeeManager

def print_menu():
    print("\n" + "*" * 30)
    print("| {:<25} |".format("1. Display all employee data"))
    print("| {:<25} |".format("2. Add a new employee"))
    print("| {:<25} |".format("3. Remove an employee"))
    print("| {:<25} |".format("4. Update employee information"))
    print("| {:<25} |".format("5. Sort employees by last name"))
    print("| {:<25} |".format("0. Exit"))
    print("*" * 30)

def get_validated_input(prompt, validator_func):
    while True:
        user_input = input(prompt)
        if validator_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def main():
    file_path = "employees.txt"
    manager = EmployeeManager(file_path)

    while True:
        print_menu()
        user_choice = input("Select an option: ")

        if user_choice == "1":
            manager.display_all_employees()
        elif user_choice == "2":
            first_name = get_validated_input("Enter first name: ", lambda x: x.isalpha())
            last_name = get_validated_input("Enter last name: ", lambda x: x.isalpha())
            phone_number = get_validated_input("Enter phone number: ", lambda x: x.isdigit() and len(x) == 10)
            email = get_validated_input("Enter email address: ", lambda x: "@" in x and "." in x)
            address = input("Enter address: ")
            position = input("Enter position: ")
            new_employee = Employee(first_name, last_name, "", phone_number, email, address, position)
            manager.add_employee(new_employee)
            print("Employee successfully added.")
        elif user_choice == "3":
            employee_to_remove = manager.get_employee_choice()
            if employee_to_remove:
                manager.remove_employee(employee_to_remove)
                print(f"Employee {employee_to_remove.first_name} {employee_to_remove.last_name} successfully removed.")
            else:
                print("Invalid choice. Please select a valid employee.")
        elif user_choice == "4":
            employee_to_update = manager.get_employee_choice()
            if employee_to_update:
                manager.update_employee_info(employee_to_update)
            else:
                print("Invalid choice. Please select a valid employee.")
        elif user_choice == "5":
            manager.sort_employees_by_last_name()
        elif user_choice == "0":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
