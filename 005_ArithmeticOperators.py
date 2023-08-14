# Augmented assignment operators
friends = 0
friends += 5    
friends -= 2
friends *= 3
friends /= 3
friends **= 2
friends %= 2
print(f"Friends = {friends}\n")

# built in functions
a = 3.24567
print(round(a))
b = -98
print(abs(b))
c = pow (2, 3)
print(c)
d,e = 5,6
print(max(d,e))
print(min(d,e),"\n")

# Math module
import math

print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(10.1))
print(math.floor(9.9),"\n")

# Calculate Circumference and Area
radius = float(input("Enter radius = "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)
print(f"Area = {round(area, 2)}cm^2")
print(f"Circumference = {round(circumference, 2)}cm\n")

# Hypotenuse
adjacent = float(input("Enter adjacent side length: "))
opposite = float(input("Enter opposite side length: "))
hypotenuse = math.sqrt(pow(adjacent, 2) + pow(opposite, 2))
print(f"Hypotenuse = {hypotenuse}")