numeros = [876, 432, 1023, 987, 654, 321, 777, 888, 999, 111]

total = sum(numeros)

print(total)


# Exercicio
numeros = [876, 432, 1023, 987, 654, 321]
soma = 0  # Variável acumuladora

for numero in numeros:
    soma += numero  # Soma cada número da lista
    #soma = soma + numero
print(f"A soma total é: {soma}")

# Pegando o maior valor

numeros2 = [199, 80, 70, 50, 30]
soma2 = 0
for maior in numeros2:
    soma2 += maior

print(f"O maior valor é {max(numeros2)}")
