# Python temperature converter

mode = int(input("Modes: \n\
1 - Celsius to Fahrenheit\n\
2 - Fahrenheit to Celsius\n\
Your Choice [1/2]?: "))

if mode == 1:
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = round((9 * celsius) / 5 + 32, 2)
    print(f"{celsius}C in fahrenheit = {fahrenheit}F")
elif mode == 2:
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = round((fahrenheit - 32) * 5 / 9, 2)
    print(f"{fahrenheit}F in celsius = {celsius}C")
else:
    print(f"{mode} is an Invalid choice")