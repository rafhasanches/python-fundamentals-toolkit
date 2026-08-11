## This program add all the odd numbers multiples of three between 0 and 500

n = 500
total = 0
for i in range(0, n+1):
    if i % 2 == 1 and i % 3 == 0:
        total += i
print('The sume of the odd numbers divisible by 3 is {}'.format(total))