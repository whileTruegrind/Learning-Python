import os

try:
    os.remove("TESTTEXT.txt")
except FileNotFoundError:
    print("File not found")