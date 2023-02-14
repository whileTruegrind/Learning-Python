students = ["Rick", "Morty", "Summer", "Arthur", "Heisenberg"]
students.sort()
for student in students:
    print(student)
print()
students.sort(reverse = True)
for student in students:
    print(student)
print("*****************************************")
students = ["Rick", "Morty", "Summer", "Arthur", "Heisenberg"]
sorted_students = sorted(students)
for student in students:
    print(student)
print("*****************************************")
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Krabs","C", 78)]
students.sort()
for student in students:
    print(student)
    age = lambda ages:ages[2]
students.sort(key = age)
for student in students:
    print(student)