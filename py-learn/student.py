class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age, sid, avg_grade):
        self.name = name
        self.age = age
        self.sid = sid
        self.avg_grade = avg_grade
        Student.num_students += 1
