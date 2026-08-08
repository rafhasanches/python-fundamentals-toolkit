name = input('Please enter your name: ')

name = name.lower()
name = name.split()

if 'doe' in name:
    print('The name contains Doe')
else:
    print('The name does not contain Doe')