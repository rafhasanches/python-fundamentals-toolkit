print('-------------------------------')
print('SUPER CHEAP STORE'.center(31))
print('-------------------------------')

s = count = product_count = 0
cheapest = 0
cheapest_product = ''

while True:
    product = input('Enter product name: ')

    while True:
        try:
            price = float(input('Enter price: $'))
            break
        except ValueError:
            print('Please enter a numeric value')

    s = s + price
    product_count += 1

    if price > 1000:
        count += 1

    if product_count == 1:
        cheapest = price
        cheapest_product = product

    elif price < cheapest:
        cheapest = price
        cheapest_product = product

    end = input('Do you want to keep going? (Y/N): ').strip().lower()

    while end != 'y' and end != 'n':
        end = input('Do you want to keep going? (Y/N): ').strip().lower()

    if end == 'n':
        break

print('-------------------------------')
print('FINAL PURCHASE'.center(31))
print('-------------------------------')

print(f'Your total is ${s}.')
print(f'The amount of products that cost more than $1000 is {count}.')
print(f'The cheapest product is {cheapest_product}, costing ${cheapest:.2f}.')


