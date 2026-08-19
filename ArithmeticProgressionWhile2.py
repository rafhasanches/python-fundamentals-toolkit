start = int(input('Enter the start number of our PA: '))
difference = int(input('Enter the difference of our PA: '))

result = start
counter = 1
print(result)

while counter < 10:
    result = result + difference
    counter += 1
    print(result)

counter = 0
extra = int(input('Enter how many extra numbers of our PA you want (0 to end program): '))

while extra != 0:
    counter = 0

    while counter < extra:
        result = result + difference
        counter += 1
        print(result)
    extra = int(input('Enter how many extra numbers of our PA you want (0 to end program): '))

print('Program ended')