class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Tester"]
        return position in valid_positions

employee1 = Employee("Eugene", "Tester")
employee2 = Employee("Alice", "Developer")
employee3 = Employee("Bob", "Manager")

print(Employee.is_valid_position("Developer"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
