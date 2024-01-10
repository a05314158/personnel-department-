Employee Management System
Overview
The Employee Management System is a command-line application designed to streamline the management of employee data within an organization. It provides functionalities such as adding new employees, updating their information, and displaying a sorted list based on last names.

if you want start programm. Start main faile 

Project Structure
The project consists of three main files:

employee.py:

Defines the Employee class for storing employee information.
The class includes an initializer (__init__) to set up the employee's attributes and a method (display_info) to display the information.
employee_manager.py:

Contains the EmployeeManager class responsible for managing employee data.
The class includes methods for loading, saving, adding, removing, updating, sorting, and displaying employee information.
Utilizes a decorator (display_employee_list) to handle scenarios where there are no employees in the list.
main.py:

Serves as the command-line interface for interacting with the system.
Provides a menu for users to choose various options such as displaying all employees, adding a new employee, removing an employee, updating employee information, sorting employees by last name, and exiting the program.
Utilizes input validation to ensure accurate user inputs.

