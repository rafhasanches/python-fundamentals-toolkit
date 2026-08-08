import random

randomnumber = random.randint(1, 5)

userNumber = int(input('Enter a number between 0 and 5: '))

if userNumber == randomnumber:
    print('You got the right number!')
else:
    print('You got the wrong number, the right number was {}'.format(randomnumber))