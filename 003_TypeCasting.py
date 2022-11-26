# Typecasting
    ## The process of converting a value of one data type to another
    ## Explicit vs Implicit

# Explicit
name = "Rishi"
age = 19
gpa = 8.9
student = True
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of gpa: {type(gpa)}")
print(f"Type of student: {type(student)}\n")

print(f"gpa as int = {int(gpa)}")
print(f"student as str = {str(student)}")
print(f"age as boolean = {bool(age)}\n")          # Anything other than zero is true

# Implicit
x = 2
y = 2.0
z = x / y
print(type(z))