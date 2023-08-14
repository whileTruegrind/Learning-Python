try:
    #with open("D:\\Coding\\Python\\Learning Python\\TESTTEXT.txt") as file:
    with open("TESTTEXT","w") as file:
        file.write("Hello World")
    print(file.closed)
except FileNotFoundError:
    print("File not found!")