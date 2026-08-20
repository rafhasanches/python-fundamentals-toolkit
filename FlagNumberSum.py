n = cont = s = 0

while True:
    n = int(input('Enter a number (999 to stop): '))
    if n == 999:
        break
    cont += 1
    s += n

print(f'You entered {cont} numbers and the sum is {s}')