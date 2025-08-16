enemies = 1


# Escopo local
def increase_enemies():
    enemies = 2
    print(f"inimigos dentro da função {enemies}")


# Escopo global
increase_enemies()
print(f"inimigos fora da função {enemies}")    