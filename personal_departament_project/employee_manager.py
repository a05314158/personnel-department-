# employee_manager.py
import csv
from employee import Employee

class EmployeeManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.employees = self.load_data()

    def load_data(self):
        employees = []
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employee = Employee(**row)
                    employees.append(employee)
        except FileNotFoundError:
            pass
        return employees

    def save_data(self):
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['first_name', 'last_name', 'middle_name', 'phone_number', 'email', 'address', 'position']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for employee in self.employees:
                writer.writerow(vars(employee))

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

    def display_all_employees(self):
        for employee in self.employees:
            employee.display_info()
            print("-------------")
