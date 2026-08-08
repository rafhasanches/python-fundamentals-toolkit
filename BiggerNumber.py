n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

if n1 > n2 and n1 > n3:
    print('The first number is the greater number')
elif n2 > n1 and n2 > n3:
    print('The second number is the greater number')
elif n3 > n1 and n3 > n2:
    print('The third number is the greater number')

if n1 < n2 and n1 < n3:
    print('The first number is the lesser number')
elif n2 < n1 and n2 < n3:
    print('The second number is the lesser number')
elif (n3 < n1 and n3 < n2):
    print('The third number is the lesser number')