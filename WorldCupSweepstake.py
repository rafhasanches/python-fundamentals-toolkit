import random

aNames = []

countries = [
['Germany' ,9],
['Croatia' ,10], 
['Argentina' ,1],
['France' ,2],
['United States' ,15],
['Mexico' ,16],
['Japan' ,17],
['Senegal' ,18],
['England' ,3],
['Spain' ,5],
['Portugal' ,6],
['Netherlands' ,7],
['Belgium' ,8],
['Brazil' ,4],
['Morocco' ,11],
['Uruguay' ,13],
['Colombia' ,14],
['Iran' ,19],
['Switzerland' ,20], 
['Sweden' ,28],
['Poland' ,29],
['Egypt' ,31],
['Nigeria' ,32],
['Denmark' ,21],
['Austria' ,22], 
['South Korea' ,23], 
['Australia' ,24], 
['Ukraine' ,25], 
['Turkey' ,26], 
['Ecuador' ,27], 
['Algeria' ,33],
['Panama' ,34], 
['Canada' ,35], 
['Tunisia' ,36], 
['Serbia' ,37], 
['Paraguay' ,38], 
['Czech Republic' ,39], 
['Norway' ,40], 
['Scotland' ,42], 
['Ivory Coast' ,43], 
['Saudi Arabia' ,49], 
['Qatar' ,51], 
['South Africa' ,56], 
['Jordan' ,62], 
['Uzbekistan' ,64], 
['Bosnia and Herzegovina' ,70], 
['Haiti' ,83], 
['New Zealand' ,85]
]

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