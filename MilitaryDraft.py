# In Brazil, every men has to apply for military service in the year that they turn 18
# This program should let the user know if this year is the year they have to present themselves, if already happened
# or if it is going to happen. The program will show the amount of years missing or passed since the moment of the duty

from datetime import datetime, timezone

current_year = datetime.now(timezone.utc).year

user_year = int(input('Enter the year you were born: '))

age = current_year - int(user_year)

if age == 18:
    print('This is the year you have to present yourself to the Brazilian Forces.')
elif age < 18:
    print('You do not have to present yourself to the Brazilian Forces this year. Only in {} year(s).'.format(18-age))
else:
    print('You should have presented yourself to the Brazilian Forces {} year(s) ago.'.format(age-18))