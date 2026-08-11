start = int(input('Enter the start number of our PA: '))
difference = int(input('Enter the difference of our PA: '))

progression = []

for i in range(10):
    progression.append(start)
    start += difference

print(progression)