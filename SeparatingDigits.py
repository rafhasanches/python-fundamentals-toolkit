while True:
    number = int(input('Enter a number between 0 and 9999: '))

    if number < 0 or number > 9999:
        print('FAIL! Please enter a number between 0 and 9999')
        continue

    thousand = number // 1000
    hundred = (number - (thousand * 1000)) // 100
    ten = (number - ((thousand * 1000) + (hundred * 100))) // 10
    unit = (number - ((thousand * 1000) + (hundred * 100) + (ten * 10)))
    print('Thousands: {}'.format(thousand))
    print('Hundred: {}'.format(hundred))
    print('Ten: {}'.format(ten))
    print('Unit: {}'.format(unit))
    break