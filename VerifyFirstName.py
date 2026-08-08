city = input('Please enter your city: ')

city = city.split()

if city[0].upper() == 'SANTO':
    print('The first word of the city name is Santo')
else:
    print('The first word of the vity name is not Santo')
