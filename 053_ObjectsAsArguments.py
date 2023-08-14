class Student:
    def __init__(self, name):
        self.name = name

def changeName(student, name):
    student.name = name

student1= Student("Rick")
print(student1.name)

changeName(student1, "Morty")
print(student1.name)