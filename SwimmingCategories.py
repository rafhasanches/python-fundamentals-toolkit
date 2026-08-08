# This program allows the user to know exactly which category the athlete should compete in.

from datetime import datetime, timezone

current_year = datetime.now(timezone.utc).year

user_year = int(input('Enter the year the athlete was born: '))

age = current_year - int(user_year)

if age <= 9:
    print('CATEGORY: ROOKIE')
elif 9 < age <= 14:
    print('CATEGORY: BEGINNER')
elif 14 < age <= 19:
    print('CATEGORY: JUNIOR')
elif 19 < age <= 20:
    print('CATEGORY: SENIOR')
else:
    print('CATEGORY: MASTER')