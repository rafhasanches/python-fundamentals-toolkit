inventory = []

while True:
   name = input('Enter the product name: ')
   if name.upper() == 'FIM':
       break

   encontrado = False
   QTArray = len(inventory)

   for i in range(QTArray):
       if name.upper() == inventory[i].upper():
           print('Attention, product already exists')
           encontrado = True
           break

   if encontrado == False:
      inventory.append(name)


print(inventory[3])
