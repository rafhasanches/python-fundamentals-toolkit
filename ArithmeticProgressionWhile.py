start = int(input('Enter the start number of our PA: '))
difference = int(input('Enter the difference of our PA: '))

result = start
counter = 1
print(result)

while counter < 10:
    result = result + difference
    counter += 1
    print(result)