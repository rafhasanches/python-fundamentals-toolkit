import random

gameChoice = random.randint(0, 10)
playerGuess = int(input("Please enter your guess (Between 0 and 10): "))
counter = 1

while gameChoice != playerGuess:
    if playerGuess > 10 or playerGuess < 0:
        print('You entered an invalid guess. Please try again.')
        counter -= 1
    else:
        print('You guessed the wrong number. Try again!')
    counter += 1
    playerGuess = int(input("Please enter your guess (Between 1 and 10): "))

print("You guessed the correct number. You needed {} guesses".format(counter))