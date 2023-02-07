class Member:
    def __init__(self, name):
        self.name = name
class Student(Member):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
class Staff(Member):
    def __init__(self, name, staff_id):
        super().__init__(name)
        self.staff_id = staff_id

student1 = Student("Rishi", 978)
staff1 = Staff("John Doe", 567)

print(student1.name)
print(student1.student_id)
print()
print(staff1.name)
print(staff1.staff_id)