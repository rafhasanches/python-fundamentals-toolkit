n = int(input('Enter a number: '))
total = 0
count = 0

while n != 999:
    total = total + n
    count += 1
    n = int(input('Enter a number: '))

print(f'You entered {count} numbers and their sum was {total}.')