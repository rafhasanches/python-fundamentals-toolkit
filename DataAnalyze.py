n = int(input('Enter a number: '))
total = 0
count = 0
greater = n
smaller = n
answer = ''

while answer != 'no':
    total = total + n
    count += 1

    if n > greater:
        greater = n

    if n < smaller:
        smaller = n

    answer = input('Do you want to continue? (yes/no): ').strip().lower()

    if answer == 'yes':
        n = int(input('Enter a number: '))

avg = total/count

print(avg, greater, smaller)