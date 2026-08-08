cpf = input("Digite os 9 primeiros digitos do CPF (sem . ou -): ")
tamanho = 9

if len(cpf) != tamanho:
    print("campo incorreto, tamanha invalido")
    exit()

print("CPF valido")
n1 = int(cpf[0:1])
n2 = int(cpf[1:2])
n3 = int(cpf[2:3])
n4 = int(cpf[3:4])
n5 = int(cpf[4:5])
n6 = int(cpf[5:6])
n7 = int(cpf[6:7])
n8 = int(cpf[7:8])
n9 = int(cpf[8:9])

m1 = n1 * 10
m2 = n2 * 9
m3 = n3 * 8
m4 = n4 * 7
m5 = n5 * 6
m6 = n6 * 5
m7 = n7 * 4
m8 = n8 * 3
m9 = n9 * 2

s1 = m1 + m2 + m3 + m4 +  m5 + m6 + m7 + m8 + m9

resto = s1 % 11

if resto < 2:
    d1 = 0
else:
    d1 = 11 - resto

m1 = n1 * 11
m2 = n2 * 10
m3 = n3 * 9
m4 = n4 * 8
m5 = n5 * 7
m6 = n6 * 6
m7 = n7 * 5
m8 = n8 * 4
m9 = n9 * 3
m10 = d1 * 2

s2 = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10

resto2 = s2 % 11
if resto2 < 2:
    d2 = 0
else:
    d2 = 11 - resto2

print('O CPF completo é: ' + cpf[0:3]+ '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + str(d1) + str(d2))