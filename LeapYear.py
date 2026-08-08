year = int(input('Enter a year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('The year of {} is a leap year'.format(year))
else:
    print('The year of {} is not a leap year'.format(year))