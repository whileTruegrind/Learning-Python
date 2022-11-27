# Python weight converter

mode = int(input("Modes: \n\
1 - Pounds to Kilograms\n\
2 - Kilograms to Pounds\n\
Your Choice [1/2]?: "))

if mode == 1:
    pounds = float(input("Enter weight in pounds: "))
    kilo = pounds / 2.205
    print(f"{pounds}lbs in kilograms = {round(kilo, 2)}kg")
elif mode == 2:
    kilo = float(input("Enter weight in kilograms: "))
    pounds = kilo * 2.205
    print(f"{kilo}kg in pounds = {round(pounds, 2)}lbs")
else:
    print(f"{mode} is an Invalid choice")