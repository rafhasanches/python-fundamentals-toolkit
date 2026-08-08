import math

angle = int(input('Enter the angle: '))

angle1 = math.radians(angle)

sin = math.sin(angle1)
cos = math.cos(angle1)
tan = math.tan(angle1)

print('{} degrees\nThe sine is {:.2f}\nThe cosine is {:.2f}\nThe tangent is {:.2f}'.format(angle, sin, cos, tan))
