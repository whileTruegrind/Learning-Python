# Default Arguments
    ## A default value for certain parameters
    ## Default is used when the argument is omitted
    ## Make your functions more flexible, reduces number of arguments

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(f"Price = {net_price(500)}")
print(f"Price with coupon = {net_price(500, 0.1)}")

# EXERCISE: Count up timer

import time

def countUp(end, start = 1):                   
    for i in range(start, end+1):
        print(i, end = " ")
        time.sleep(1)
    print("TIME'S UP!\n")

countUp(10, 5)
countUp(10)