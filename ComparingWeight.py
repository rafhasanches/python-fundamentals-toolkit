n = 5

for i in range(1, n + 1):
    weight = int(input('Enter your weight: '))
    if i == 1:
        max_weight = weight
        min_weight = weight
    else:
        if weight > max_weight:
            max_weight = weight
        if weight < min_weight:
            min_weight = weight

print('The highest weight is {} and the lowest weight is {}.'.format(max_weight, min_weight))