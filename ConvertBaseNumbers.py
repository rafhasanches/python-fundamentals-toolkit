number = int(input('Enter a number: '))
choice = int(input('Press 1 for BINARY 2 for OCTAL 3 for HEXADECIMAL: '))

if choice == 1:
    print('Binary: {:b}'.format(number))
elif choice == 2:
    print('Octal: {:o}'.format(number))
elif choice == 3:
    print('Hexadecimal: {:X}'.format(number))