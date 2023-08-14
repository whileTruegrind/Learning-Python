# variable:
    ## A reusable container for storing a value
    ## A variable behaves as if it were the value it contains
# Basic types:
    ## Integer
    ## Float
    ## String
    ## Boolean

# Integer, int
age = 21
#print("You are",age,"years old")
#print("You are " + str(age)+ " years old")
print(f"You are {age} years old")

# Float, float
gpa = 8.9
print(f"Your GPA is {gpa}")

# String, str
name = "Rishi"
print(f"Hi, {name}")

# Boolean, bool
student = True
print(f"Student?: {student}")

# Tricks
x, y ,z = 1, 2, 3
print(x, y, z)
x = y = z = 1
print(x , y, z)