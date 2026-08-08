len1 = int(input('Enter the length of the first side of your triangle: '))
len2 = int(input('Enter the length of the second side of your triangle: '))
len3 = int(input('Enter the length of the third side of your triangle: '))

if len1 + len2 > len3 and len1 + len3 > len2 and len2 + len3 > len1:
    print('These sides can form a triangle')

    if len1 == len2 == len3:
        print('Equilateral triangle')
    elif len1 == len2 or len1 == len3 or len2 == len3:
        print('Isoceles triangle')
    else:
        print('Scalene triangle')

else:
    print('These sides cannot form a triangle')