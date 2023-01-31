try:
    #with open("D:\\Coding\\Python\\Learning Python\\TESTTEXT.txt") as file:
    with open("test.txt") as file:
        print(file.read())            # Closes file automatically 
    print(file.closed)
except FileNotFoundError:
    print("File not found!")