# while loop = Execute some code WHILE some condition is true

name = ""

while name == "":
    name = input("Your name?: ")
    if name == "":
        print("Enter a name!")
print(f"Hi, {name}\n")

number = -1
while number < 0 or number > 10:
    number = int(input("Enter a number between 1 to 10: "))
    if number < 0 or number > 10:
        print("Invalid!")
print(f"Your number = {number}")