import json
from employee import Employee

def display_employee_list(func):
    def wrapper(manager):
        employees = manager.employees
        if employees:
            func(manager)
        else:
            print("No employees in the list.")
    return wrapper

class EmployeeManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.employees = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                employees = [Employee(**employee_data) for employee_data in data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("File not found or invalid JSON format. Creating a new one.")
            employees = []
        return employees

    def save_data(self):
        with open(self.file_path, mode='w', encoding='utf-8') as file:
            data = [employee.__dict__ for employee in self.employees]
            json.dump(data, file, ensure_ascii=False, indent=2)

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        self.save_data()

    def remove_employee(self, employee: Employee):
        self.employees.remove(employee)
        self.save_data()

    def update_employee_info(self, employee: Employee):
        print(f"Updating information for {employee.first_name} {employee.last_name}")
        employee.phone_number = input("Enter new phone number: ")
        employee.email = input("Enter new email address: ")
        employee.address = input("Enter new address: ")
        employee.position = input("Enter new position: ")
        self.save_data()

    @display_employee_list
    def sort_employees_by_last_name(self):
        self.employees = sorted(self.employees, key=lambda x: x.last_name)
        self.display_all_employees()

    def get_employee_by_index(self, index: int):
        return self.employees[index - 1] if 1 <= index <= len(self.employees) else None

    @display_employee_list
    def display_all_employees(self):
        print("\nEmployee List:")
        print("*" * 94)
        print("| {:<4} | {:<15} | {:<15} | {:<15} | {:<20} | {:<20} |".format("ID", "First Name", "Last Name", "Position", "Phone Number", "Email"))
        print("*" * 94)
        for i, employee in enumerate(self.employees, start=1):
            print("| {:<4} | {:<15} | {:<15} | {:<15} | {:<20} | {:<20} |".format(i, employee.first_name, employee.last_name, employee.position, employee.phone_number, employee.email))
        print("*" * 94)

    def get_employee_choice(self):
        self.display_all_employees()
        choice = input("Select an employee (enter the number): ")
        return self.get_employee_by_index(int(choice))
