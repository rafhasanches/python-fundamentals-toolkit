days = float(input('Enter the amount of days you stayed with the car: '))
km = float(input('Enter the amount of kilometers driven: '))

costday = 60
costkm = 0.15

total = (costday * days) + (costkm * km)

print('The total cost of your car is ${:.2f}'.format(total))
