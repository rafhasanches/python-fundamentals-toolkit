num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

if num1 > num2:
    print('The number {} is bigger than the number {}'.format(num1, num2))
elif num1 < num2:
    print('The number {} is bigger than the number {}'.format(num2, num1))
else:
    print('The two numbers are equal')