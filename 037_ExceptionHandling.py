# Exception: Events detected during execution that interrupt thr flow of a program

try:
    numerator = int(input("Numerator?: "))
    denominator = int(input("Denominator?: "))
    result = numerator/denominator
except ZeroDivisionError as E:
    print(E)
    print("Can't divide by zero!")
except ValueError:
    print("Enter numbers only")
except Exception:
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("Will always execute")