tripDistance = int(input('Enter a trip distance: '))

if tripDistance <= 200:
    tripCost = tripDistance * 0.5
    print('Your trip cost is ${}'.format(float(tripCost)))
elif tripDistance > 200:
    tripCost = tripDistance * 0.45
    print('Your trip cost is ${}'.format(float(tripCost)))