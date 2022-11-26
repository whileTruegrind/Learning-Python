operator = input("Enter an operator [+, -, *, /]: ")
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")

print(f"{num1} {operator} {num2} = {result}")