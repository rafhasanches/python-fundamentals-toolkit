speed = int(input('What was the car speed? '))
overspeed = speed - 80
ticket = overspeed * 7
if speed > 80:
    print('Your speed was {}km/h above 80km/h, your ticket is: ${}'.format(overspeed, ticket))
else:
    print('You are under the permit speed, have a nice trip!')