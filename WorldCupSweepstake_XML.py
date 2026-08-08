import random
import xml.etree.ElementTree as ET

aNames = []
countries = []




tree = ET.parse('FIFARanking.xml')
root = tree.getroot()

for country in root:
    name = country.find('name').text
    ranking = int(country.find('ranking').text)

    countries.append([name,ranking])

countries.sort(key=lambda x: x[1]) # classificacao array  pelo RANKING FIFA

#count = len(countries)
#choice = random.randint(0,count - 1)  # exemplo sorteio, usamos "count - 1" pois o primeiro indice do array é ZERO

#print(choice + 1)  mopstra indice que foi sorteado
#print(countries[choice][0]) mostra o conteudo do array , coluna ZERO

while True:
    name = input("Enter your name: (END to finish): ")
    if name.upper() == "END":
        break
    # rotina de validacao do apostador (name)
    NomeEncontrado = False
    QTArray = len(aNames)

    for i in range(QTArray):
        # print('analisando nome',aNames[i][0].upper() )
        if name.upper() == aNames[i][0].upper():
            print('This person was already added to the list')
            NomeEncontrado = True
            break

    if NomeEncontrado == False:
        aNames.append( [name, ''] )

QTArray = len(aNames)
# print('inicio sorteio paises',QTArray,' nomes')
# rotina sorteio de numero randomico do Pais

for i in range(QTArray):

    while True:
        choiceError = False
        choice = random.randint(0, QTArray - 1)
        # print('pais sorteado',choice)

        for j in range(i):
            if aNames[j][1] == choice:
                choiceError = True
                break

        if choiceError == False:
            break

    aNames[i][1] = choice
print('Resultado final:')
for i in range(QTArray):
    nCodigoPais= aNames[i][1]
    print( aNames[i][0],' -> ', countries[nCodigoPais] [0]  )