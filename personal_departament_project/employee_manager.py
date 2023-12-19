from employee import Employee
def display_employee_list(func):
    def wrapper(manager, *args, **kwargs):
        employees = manager.employees
        if employees:
            print("\nEmployee List:")
            print("*" * 94)
            print("| {:<4} | {:<15} | {:<15} | {:<15} | {:<20} | {:<20} |".format("ID", "First Name", "Last Name", "Position", "Phone Number", "Email"))
            print("*" * 94)
            for i, employee in enumerate(employees, start=1):
                print("| {:<4} | {:<15} | {:<15} | {:<15} | {:<20} | {:<20} |".format(i, employee.first_name, employee.last_name, employee.position, employee.phone_number, employee.email))
            print("*" * 94)
        else:
            print("No employees in the list.")
        return func(manager, *args, **kwargs)

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
            pass
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

    def update_employee(self, old_employee, new_employee):
        index = self.employees.index(old_employee)
        self.employees[index] = new_employee
        self.save_data()

    @display_employee_list
    def display_all_employees(self):
        pass

    def get_employee_by_index(self, index):
        return self.employees[index - 1] if 1 <= index <= len(self.employees) else None
