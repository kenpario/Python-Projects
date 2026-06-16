class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "No students to calculate average GPA."
        return f"Average GPA: {cls.total_gpa/cls.count:.2f}"


student1 = Student("Alice", 3.5)
student2 = Student("Bob", 3.8)
student3 = Student("Charlie", 3.2)

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())
print(Student.get_count())
print(Student.get_average_gpa())
