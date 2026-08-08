import random

st1 = input('Name of the first student: ')
st2 = input('Name of the second student: ')
st3 = input('Name of the third student: ')
st4 = input('Name of the fourth student: ')

presentation_order = [st1, st2, st3, st4]

random.shuffle(presentation_order)

print('The order is the following: {}'.format(presentation_order))