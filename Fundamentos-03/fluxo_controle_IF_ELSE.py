"""
Operadores de comparação
==   igual
!=   diferente
<    menor
>    maior
<=   menor igual
>=   maior igual
"""


# Exercício

numero_a_verificar = int(input('Digite um número: '))

print(numero_a_verificar % 2)

if numero_a_verificar % 2 == 0:
    print('O número é par')
else:
    print('Onúmero é ímpar')