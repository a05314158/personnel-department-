from employee import Employee

def display_employee_list(func):
    def wrapper(manager, *args, **kwargs):
        employees = manager.employees
        if employees:
            func(manager, *args, **kwargs)
        else:
            print("No employees in the list.")
    return wrapper

class EmployeeManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.employees = self.load_data()

    def load_data(self):
        employees = []
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                for line in file:
                    data = line.strip().split(',')
                    employee = Employee(*data)
                    employees.append(employee)
        except FileNotFoundError:
            print("File not found. Creating a new one.")
        return employees

    def save_data(self):
        with open(self.file_path, mode='w', encoding='utf-8') as file:
            for employee in self.employees:
                data = [employee.first_name, employee.last_name, employee.middle_name,
                        employee.phone_number, employee.email, employee.address, employee.position]
                line = ','.join(data) + '\n'
                file.write(line)

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_data()

    def remove_employee(self, employee):
        self.employees.remove(employee)
        self.save_data()

    def update_employee_info(self, employee):
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

    def get_employee_by_index(self, index):
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
