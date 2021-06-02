# Random number generetor
# guess round Game
# main
import random


def enemy_ship(dificulty):
    enemy_ship_row = random.randint(1, dificulty)
    enemy_ship_col = random.randint(1, dificulty)
    enemy_ship_pos = [enemy_ship_row, enemy_ship_col]
    return enemy_ship_pos


def guess():
    guess_row = input("Make your guess! \nRow: ")
    guess_col = input("Collumn: ")
    guessed_answered = [int(guess_row), int(guess_col)]
    return guessed_answered


def game():
    dificulty = 10
    enemy_ship_pos = enemy_ship(dificulty)
    if enemy_ship_pos == guess():
        print("HIT!")
    else:
        print(f"MISS! enemy ship was at {enemy_ship_pos}")


game()
