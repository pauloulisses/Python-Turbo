# Criando uma lista simples com nomes de frutas
frutas = ['Banana', 'manga', 'Uva']
print(frutas)  # Imprime a lista de frutas

# Criando uma lista com os 26 estados brasileiros + o Distrito Federal
# Corrigindo o erro de digitação no primeiro estado: "AAcre" -> "Acre"
brazilian_states = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia",
    "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão",
    "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba",
    "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte",
    "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo",
    "Sergipe", "Tocantins"
]

# Imprimindo a lista de estados
print(brazilian_states)

# Acessando o item de índice 1 (segundo da lista)
print(brazilian_states[1])  # Saída: "Alagoas"

# Acessando o último elemento da lista usando índice negativo
print(brazilian_states[-1])  # Saída: "Tocantins"

# Adicionando um novo estado fictício ao final da lista com append()
# append() adiciona o item como um único elemento
brazilian_states.append('TipsLand')
print(brazilian_states)  # 'TipsLand' aparece no final da lista

# Adicionando dois novos elementos fictícios usando extend()
# extend() adiciona cada item do iterável separadamente na lista
brazilian_states.extend(['Jerusalem', 'Israel'])
print(brazilian_states)  # Agora a lista inclui 'Jerusalem' e 'Israel' no final

