# input (): 
    ## This function first takes the input from the user and converts it into a string. 
    ## The type of the returned object always will be <type ‘str’>. 
    ## It does not evaluate the expression it just returns the complete statement as String. 
    ## For example, Python provides a built-in function called input which takes the input from the user. 
    ## When the input function is called it stops the program and waits for the user’s input. 
    ## When the user presses enter, the program resumes and returns what the user typed. 

name = input("Enter your name: ")
print(f"Hello {name}")

# Mad libs game
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")
print(f"Today I went to a {adjective1} zoo")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

# Calculate area of Rectangle
length = int(input("Enter length of a rectangle: "))
width = int(input("Enter width of rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area = {area}")
print(f"Perimeter = {perimeter}")

# Shopping cart
item = input("Item name?: ")
price = float(input("Price?: "))
quantity = int(input("Quantity?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total = ${round(total, 2)}")