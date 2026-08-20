import random

n = s = count = 0

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Let\'s play EVEN AND ODDS!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

while True:
    n = int(input('Enter a number between 0 and 10: '))
    result = ''
    if n > 10:
        print('Invalid number. Start again')
        break

    choice = (input('Do you want even or odd? (E/O)')).strip().lower()

    computerChoice = random.randint(0, 10)
    s = n + computerChoice

    if s % 2 == 0:
        result = 'e'
    else:
        result = 'o'

    print(f'The sum between {n} and {computerChoice} is {s}')

    if choice == result:
        print('You WON. Let\'s play again!')
        count += 1
    else:
        print('You LOST.')
        break
print(f'You have won {count} time(s).')

