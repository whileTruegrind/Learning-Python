import random
import string

characters = " " + string.punctuation + string.digits + string.ascii_letters
characters = list(characters)

key = characters.copy()
random.shuffle(key)

text = input("Enter a message to encrypt: ")
cipher = ""

for letter in text:
    index = characters.index(letter)
    cipher += key[index]

print(f"Original Text: {text}")
print(f"Encrypted Text: {cipher}")