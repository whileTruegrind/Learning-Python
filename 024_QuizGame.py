# Python quiz game

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ QUIZ GAME ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
questions = ("1 - What was Meta Platforms Inc formerly known as?",
             "2 - The logo for luxury car maker Porsche features which animal?",
             "3 - Suriname is located on which continent?")

options = (("a. Facebook", "b. Lizard Co.", "c. Privacy Zucked", "d. LifeInvader"),
           ("a. Cheetah", "b. Horse", "c. Bull", "d. Lion"),
           ("a. Africa", "b. Asia", "c. South America", "d. Europe"))

answers = ("a. Facebook", "b. Horse", "c. South America")

guesses = []

score = 0

for i in range(0,len(questions)):
    print(questions[i])
    for j in range(0,4):
        print(f"    {options[i][j]}")
    guess = input("Your Answer? [a (or) b (or) (or) c (or) d]: ")
    guesses.append(guess)
    if guesses[i].lower() == answers[i][0]:
        print("Correct!")
        score += 100
    else:
        print("Wrong!")
        print(f"Correct answer: {answers[i]}")
    print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ QUIZ ENDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(f"YOUR SCORE: {score}")