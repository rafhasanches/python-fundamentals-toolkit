n = 4
sum = 0
oldest_age = 0
oldest_name = ""
under_20_female = 0

for i in range(n):
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    sex = input('Are you a MALE or FEMALE? ').strip().lower()
    sum += age

    if sex == 'male' and age > oldest_age:
            oldest_age = age
            oldest_name = name

    if sex == 'female' and age < 20:
        under_20_female += 1

avg = sum / n

print('The average age of everybody is {}, the oldest man name is {} and there are {} women younger than 20 years old'.format(avg, oldest_name, under_20_female))

