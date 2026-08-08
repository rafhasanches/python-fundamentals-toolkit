print('Welcome to the Rafha Bank, please insert the values required.')
homeValue = int(input('Please enter the home loan value: '))
salary = int(input('Please enter your monthly salary: '))
years = int(input('Please enter the number of years you want to pay: '))
installment = homeValue / (years * 12)

if installment > (salary * 0.3):
    print('LOAN DENIED')
else:
    print('LOAN APPROVED')
    print('Your monthly installment is:${:.2f}'.format(installment))
