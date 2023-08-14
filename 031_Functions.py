# function:
    ## A block of reusable code
    ## place () after the function name to invoke it

def add(num1, num2):
    return num1 + num2

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))

print(f"{num1} + {num2} = {add(num1, num2)}")