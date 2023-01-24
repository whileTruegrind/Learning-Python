import random

options = ("rock", "paper", "scissors")
computer = random.choice(options)

player = 0
while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ")
    player = player.lower()
    if player not in options:
        print(f"{player} is invalid!")

print(f"Computer choice : {computer}")
print(f"Your choice     : {player}")

if computer == player:
    print("It's a tie!")
elif player == "rock" and computer == "paper":
    print("You lose!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "paper" and computer == "scissors":
    print("You lose!")
elif player == "scissors" and computer == "rock":
    print("You lose!")
elif player == "scissors" and computer == "paper":
    print("You win!")