sex = input('Please enter your sex (M or F): ').strip().lower()

while sex != 'm' and sex != 'f':
    print('You entered an invalid digit. Please try again.')
    sex = input('Please enter your sex (M or F): ').strip().lower()


print("Valid input:", sex)