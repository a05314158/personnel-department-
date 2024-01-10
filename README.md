Employee Management System
Overview
The Employee Management System is a command-line application designed to streamline the management of employee data within an organization. It provides functionalities such as adding new employees, updating their information, and displaying a sorted list based on last names.

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
Getting Started
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/employee-management-system.git
Navigate to the Project Directory:

bash
Copy code
cd employee-management-system
Run the Program:

bash
Copy code
python main.py
Usage
Upon running the program, a menu will be displayed, allowing you to perform various actions on the employee data.

Follow the prompts to add, remove, update, or display employee information.

The system utilizes a text file (employees.txt) to persistently store employee data.

Dependencies
The project has no external dependencies beyond Python 3.x.

Future Enhancements
Integration with databases for improved scalability.
Implementation of a web interface for user-friendly interaction.
Contributors
[Your Name]
[Contributor 1]
[Contributor 2]
License
This project is licensed under the MIT License - see the LICENSE.md file for details.
