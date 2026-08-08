salary = float(input('Enter your salary: '))

if salary > 1250:
    newsalary = salary * 1.10
    print('Your new salary is ${:.2f}'.format(newsalary))
elif salary <+ 1250:
    newsalary = salary * 1.15
    print('Your new salary is ${:.2f}'.format(newsalary))