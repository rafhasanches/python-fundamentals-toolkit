n = 0

while True:
    mult = 1
    n = int(input('Enter a number you want to see the multiplication table: '))
    if n < 0:
        break
    print('--------------------------------')
    while mult <= 10:
        print(f'{n} x {mult} = {n * mult}')
        mult += 1
    print('--------------------------------')
print('Thanks for using the multiplication table!')