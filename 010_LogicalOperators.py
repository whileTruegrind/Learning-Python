# Logical Operators:
    ## and: checks two or more conditions is true
    ##  or: Checks if at least on condition is true
    ## not: True if condition is False, and vice versa

temp = 23

if temp > 0 and temp < 30:
    print("Temperature is good")
elif not (temp < 0 or temp > 100):
    print("Normal temperature")
else:
    print("Temperature is bad")