print('Seja bem-vindo(a) ao TipsPark')

altura = int(input('Qual é a sua altura em cm? '))

if altura >= 120 and altura <= 159:
    print('Vende o ingresso!')
    idade = int(input('Qual é a sua idade? '))
    if idade >= 18 and idade <= 20:
        print('O ingresso vai custar R$24 Reais')

elif altura >= 160 and altura <= 189:
    print('Vende ingresso!')
    idade = int(input('Qual a sua idade? '))
    if idade >= 21 and idade <= 25:
        print('O ingresso irá custar R$28 Reais')

elif altura >= 190 and altura <= 200:
    print('Vender ingresso!')
    idade = int(input('Qual a sua idade? '))
    if idade >= 26 and idade <= 30:
        print('O ingresso irá custar R$32 Reais')
else:
    print('Altura não permitida para os brinquedos')