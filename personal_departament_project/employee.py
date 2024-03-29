class Employee:
    def __init__(self, id: int = None, first_name: str = "", last_name: str = "", middle_name: str = "",
                 phone_number: str = "", email: str = "", address: str = "", position: str = ""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.position = position

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Middle Name: {self.middle_name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Position: {self.position}")
