n = int(input('Enter the amount of elements you want: '))
counter = 0
first = 0
second = 1
print(first)
print(second)

while counter < n - 2:
    fibonacci = first + second

    print(fibonacci)

    first = second
    second = fibonacci
    counter += 1
