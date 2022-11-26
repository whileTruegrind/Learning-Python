# if:
    ## Do some code only IF some condition is True
# Else:
    ## Do something else

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
elif age < 0:
    print("Invalid Age")
else:
    print("Ineligible")

for_sale = True
if for_sale:
    print("Buying")
else:
    print("Leaving")