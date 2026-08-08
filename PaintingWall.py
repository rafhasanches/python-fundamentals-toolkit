w = float(input('Enter the width of the wall in meters:'))
h = float(input('Enter the height of the wall in meters:'))

area = (w*h)

l = area/2

print('The amount of paint that you need to paint this wall of {:.2f}m2 is {:.2f} liters'.format(area,l))