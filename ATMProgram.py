print('-------------------------------')
print('RAFHA BANK'.center(31))
print('-------------------------------')

withdraw = int(input('How much money would you like to withdraw?'))

bill = 50

while withdraw > 0:
    quantity = withdraw // bill
    withdraw = withdraw % bill

    if quantity > 0:
        print(f'{quantity} bill(s) of ${bill}')

    if bill == 50:
        bill = 20
    elif bill == 20:
        bill = 10
    elif bill == 10:
        bill = 5
    elif bill == 5:
        bill = 1