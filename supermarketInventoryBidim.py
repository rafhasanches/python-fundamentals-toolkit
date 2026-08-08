from datetime import date, datetime

inventory = []

while True:
   name = input('Enter the product name: ')
   if name.upper() == 'FIM':
       break
   quantity = int(input('Enter the quantity: '))
   price = float(input('Enter the price: '))
   expDate = input('Enter the expiration date: ')
   dateConverted = date.strptime(expDate, '%Y/%m/%d')

   encontrado = False
   QTArray = len(inventory)

   for i in range(QTArray):
       if name.upper() == inventory[i][0].upper():
           print('Attention, product already exists')
           encontrado = True
           break

   if encontrado == False:
      inventory.append( [name,quantity,price,dateConverted] )

#inventory[0].sort(key=str.lower)

QTArray = len(inventory)
for i in range(QTArray):
    print( inventory[i][0], inventory[i][1], inventory[i][2], inventory[i][3] )

print(len(inventory))
