import datetime

n = 7
count = 0
current_year = datetime.datetime.now().year
for i in range(n):
    year_born = int(input('Enter the year you were born: '))
    age = current_year - year_born
    if age >= 21:
        count += 1

print('The number of people over 21 is {}'.format(count))