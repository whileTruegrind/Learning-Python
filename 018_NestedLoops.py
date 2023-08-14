# Nested loops:
    ## A loop within a loop
    ## outer loop:
    ##     inner loop:

for x in range(3):
    for y in range(1, 10):
        print(y, end = " ")
    print()

# Print a rectangle

symbol = input("Enter a symbol: ")
length = int(input("Enter length: "))
width  = int(input("Enter width: "))

for x in range(width):
    for y in range(length):
        print(symbol, end = "")
    print()
