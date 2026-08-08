import math

side1 = float(input('Enter the side 1: '))
side2 = float(input('Enter the side 2: '))

hypotenuse = math.hypot(side1, side2)

print('The hypotenuse of sides {} and {} is: {}'.format(side1, side2, hypotenuse))

