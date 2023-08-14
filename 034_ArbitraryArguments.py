# *args
    ## Allows you to pass multiple non-key arguments
# **kwargs
    ## Allows you to pass multiple keyword arguments
# *: Unpacking operator

#def add(num1, num2):
#    return num1 + num2

# ARGS
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1))
print(add(1,2))
print(add(1,2,3))

def display_name(*names):
    for name in names:
        print(name, end = " ")
    print()

display_name("Rishi")
display_name("Rick", "Morty")
display_name("Rick", "Morty", "Summer")
print("\n")

# KWARGS
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street = "69th street",
              city = "Chennai",
              state = "TN",
              zip = "600420")
print("\n")

# COMBINATION OF BOTH

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Mr.", "Rishi",
               street = "69th Street",
               pobox = "#1010",
               city = "Chennai",
               state = "TN",
               zip = "54321")