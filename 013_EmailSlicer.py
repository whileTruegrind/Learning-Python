# Python E-mail slicer

email = input("Enter your e-mail address: ")

username = email[ : email.index("@")]
domain = email[email.index("@") + 1 : ]

print(f"Your username: {username}")
print(f"Your domain: {domain}")