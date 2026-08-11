total = 0

for i in range(0, 6):
    n = int(input('Enter a number: '))
    if n % 2 == 0:
        total = total + n
print(total)