from datetime import date, datetime

dateInput = input('Type a date: ')

dateConverted = date.strptime(dateInput, '%Y/%m/%d')

todayDate = date.today()

differenceDate = dateConverted - todayDate

if differenceDate.days < 0:
    differenceDate = differenceDate * (-1)

print(differenceDate.days, 'days')

year = differenceDate.days // 365
remainingDays = differenceDate.days % 365

month = remainingDays // 30
day = remainingDays % 30


print(year, 'years', month, 'months', day, 'days')
