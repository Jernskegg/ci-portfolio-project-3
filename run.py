# Random number generetor
# guess round Game
# main
import random

def enemy_ship():
    enemy_ship_row = random.randint(1, 10)
    enemy_ship_col = random.randint(1, 10)
    enemy_ship_pos = [enemy_ship_row, enemy_ship_col]
    return enemy_ship_pos

print(enemy_ship())