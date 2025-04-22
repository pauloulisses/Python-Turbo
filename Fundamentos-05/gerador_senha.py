import random
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '%', '&', '(', ')', '*', '+']

nr_letters = int(input('Quantas letras você deseja em sua senha?: \n'))
nr_symbols = int(input('Quantos simbolos você deseja?:\n'))
nr_numbers = int(input('Quantos números você deseja?;\n'))

password_list = []

for char in range(0, nr_letters):
    password_list += random.choice(letters)


for char in range(0, nr_symbols):
    password_list += random.choice(symbols)

for char in range(0, nr_numbers):
    password_list += random.choice(numbers)

print(password_list)


