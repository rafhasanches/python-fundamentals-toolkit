from random import choice

st1 = input('Name of the first student: ')
st2 = input('Name of the second student: ')
st3 = input('Name of the third student: ')
st4 = input('Name of the fourth student: ')

rnd = choice([st1,st2,st3,st4])

print('The student who will clean the blackboard a is {}'.format(rnd))