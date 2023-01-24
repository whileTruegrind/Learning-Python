import random

#options = ("rock","paper","scissors")
#print(random.randint(1,20))
#print(random.random(1,20))
#print(random.choice(options))
#random.shuffle(options)
#print(options)

number = random.randint(1,100)
tries = 0

while True:
    tries += 1
    guess = int(input("Guess the number: "))
    if guess < number:
        print("Try higher")
    elif guess > number:
        print("Try lower")
    else:
        print("CORRECT!")
        print(f"Took you {tries} tries")
        break