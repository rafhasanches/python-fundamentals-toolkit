name = input('Enter your full name: ')

print('Your full name is {}'.format(name.upper()))
print('Your full name is {}'.format(name.lower()))

print('The count with spaces is {}'.format(len(name)))
letter_count = len(name.replace(' ', ''))
print('The count without spaces is {}'.format(letter_count))

first_name = name.split()[0]
print('The first name length is {}'.format(len(first_name)))
