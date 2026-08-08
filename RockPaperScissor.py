# This program will allow the user to play Rock, Paper and Scissor with the computer

import random
options = ['rock', 'paper', 'scissors']

computer_option = random.choice(options)
player_option = input('Enter your play (rock, paper, or scissor): ').lower().strip()

if player_option not in options:
    print('Invalid choice')
    exit(0)
else:
    print(f'Computer chose {computer_option}')

if player_option == computer_option:
    print('It is a tie')
elif(
    (player_option == 'rock' and computer_option == 'paper') or
    (player_option == 'paper' and computer_option == 'scissors') or
    (player_option == 'scissors' and computer_option == 'rock')
):
    print('You lost')
else:
    print('You won')