# ESCOPO GLOBAL
player_health = 10

# ESCOPO LOCAL
def drink_position():
    position_strength = 2
    print(position_strength)  # imprime variável local

    # imprimindo escopo global
    print(player_health)  # lê variável global

drink_position()

print(f"Depois da função {player_health}")
