# This program will let the user know if they passed their class, failed or they can do an extra test to pass

grade1 = float(input('Enter your first grade: '))
grade2 = float(input('Enter your second grade: '))

avg = (grade1 + grade2) / 2

print('Your average grade is {}'.format(avg))
10
if avg < 5:
    print('You failed this class')
elif 5 <= avg < 7:
    print('You are eligible to do the extra test')
else:
    print('You passed this class!')