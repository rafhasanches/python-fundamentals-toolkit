print('-------------------------------')
print('REGISTRATION'.center(31))
print('-------------------------------')

older = 0
male = 0
womanyoung = 0

while True:
    registerage = int(input('Enter your age: '))
    registersex = input('Enter your sex (M/F): ').strip().lower()

    while registersex != 'm' and registersex != 'f':
        registersex = input('Enter your sex (M/F): ').strip().lower()

    if registerage >= 18:
        older += 1

    if registersex == 'm':
        male += 1

    if registersex == 'f' and registerage < 20:
        womanyoung += 1

    end = input('Do you want to keep going? (Y/N): ').strip().lower()
    while end != 'y' and end != 'n':
        end = input('Do you want to keep going? (Y/N): ').strip().lower()

    if end == 'y':
        print('-------------------------------')
        print('REGISTRATION'.center(31))
        print('-------------------------------')
    else:
        break

print(f'There was {older} people older than 18. {male} men and {womanyoung} women younger than 20.')