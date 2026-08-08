height = float(input('Enter your height in meters (EX: 1.85): '))
weight = float(input('Enter your weight in kg: '))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print('Your BMI is {}. You are underweight'.format(bmi))
elif 18.5 <= bmi < 25:
    print('Your BMI is {}. Your weight is within the healthy range.'.format(bmi))
elif 25 <= bmi < 30:
    print('Your BMI is {}. You are overweight'.format(bmi))
elif 30 <= bmi < 40:
    print('Your BMI is {}. You are obese'.format(bmi))
else:
    print('Your BMI is {}. You are morbid obese'.format(bmi))