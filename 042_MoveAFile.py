import os

source = "D:\\Coding\\Python\\Learning Python\\TESTTEXT.txt"
destination = "D:\\Coding\\Junk\\TESTTEXT.txt"

try:
    if os.path.exists(destination):
        print("File present already")
    else:
        os.replace(source,destination)
        print(f"{source} was moved")
except FileNotFoundError:
    print("File not found")