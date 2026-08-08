cpf = input("Digite o CPF (sem . ou -): ")
tamanho = 9

s1 = 0
s2 = 0
count = 0

while count < tamanho:
    s1 += int(cpf[count]) * (10 - count)
    count += 1

if s1 % 11 < 2:
    d1 = 0
else:
    d1 = 11 - s1 % 11

count = 0
cpfx = cpf[0:9] + str(d1)

while count < tamanho:
    s2 += int(cpfx[count]) * (11 - count)
    count += 1

if s2 % 11 < 2:
    d2 = 0
else:
    d2 = 11 - s2 % 11

if str(cpf) == cpfx + str(d2):
    print('O CPF é válido!')
else:
    print('O CPF está incorreto ou é inválido!')
