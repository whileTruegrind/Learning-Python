import os

path = "D:\\Coding\\Python\\Learning Python\\TESTTEXT.txt"

if os.path.exists(path):
    print("Path exists!")
    if os.path.isfile(path):
        print("File exists!")
    elif os.path.isdir(path):
        print("This is a directory!")
else:
    print("File doesn't exist!")