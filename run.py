import random
import gspread
from google.oauth2.service_account import Credentials

# Authentication for google drive API and
# allows python to access the google spreadsheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('PROJECT3GAME')
# end of authoratization


def battle_sheet():
    tries = 5
    while tries > 0:
        try:
            sheet_number = str(random.randint(1, 10))
            battlesheet = SHEET.add_worksheet(title=sheet_number,
                                              rows="10", cols="10")
            break
        except Exception:
            if tries > 1:
                tries -= 1
            else:
                print("No battlesheet available! please try again later.")
                quit()
    return battlesheet


def enemy_ship(total_ships):
    enemysheet = battle_sheet()
    number_of_ships = 0
    while number_of_ships < total_ships:
        enemy_ship_row = random.randint(1, 10)
        enemy_ship_col = random.randint(1, 10)
        enemy_ship_pos = [enemy_ship_row, enemy_ship_col]
        enemysheet.update_cell(enemy_ship_pos[0],
                               enemy_ship_pos[1], 'o')
        number_of_ships += 1
    return enemysheet


def initiate_player(total_ships):
    game_enemy_ships = total_ships
    playersheet = battle_sheet()
    while game_enemy_ships != 0:
        position = shoot("placement")
        print(position)
        guess_try = playersheet.cell(position[0],
                                     position[1]).value
        if guess_try is None:
            playersheet.update_cell(position[0], position[1], 'o')
            game_enemy_ships -= 1
        else:
            print("You have allready positioned a ship here, Try another one")
    return playersheet


def shoot(text):
    while True:
        try:
            guess_row = input(f"Make your {text}! \nRow: ")
            if int(guess_row) > 10 or int(guess_row) < 1:
                raise ValueError("number out of range")
            guess_col = input("Collumn: ")
            if int(guess_col) > 10 or int(guess_col) < 1:
                raise ValueError("number out of range")
            guessed_answered = [int(guess_row), int(guess_col)]
            break
        except ValueError as error:
            print(f"Unkown input:{error}")
            print("please provide a number between 1 and 10.")
    return guessed_answered


def enemy_guess(playersheet):
    print("\nComputers turn")

    while True:
        computer_guess = [random.randint(1, 10), random.randint(1, 10)]
        guess_try = playersheet.cell(computer_guess[0],
                                     computer_guess[1]).value
        if guess_try == "o":
            print(f"enemy guessed {computer_guess}")
            print("ENEMY HIT!")
            playersheet.update_cell(computer_guess[0], computer_guess[1], 'x')
            return True
        elif guess_try == "x":
            continue
        else:
            print(f"enemy guessed {computer_guess}")
            print("ENEMY MISSED!")
            playersheet.update_cell(computer_guess[0], computer_guess[1], 'x')
            break


def player_guess(enemysheet):
    print("\nIt's your turn")
    while True:
        user_guess = shoot("guess")
        print(user_guess)
        guess_try = enemysheet.cell(user_guess[0],
                                    user_guess[1]).value
        if guess_try == "o":
            print("YOU HIT!")
            enemysheet.update_cell(user_guess[0], user_guess[1], 'x')
            return True
        elif guess_try == "x":
            print("You allready fired upon this coordinates, try another one.")
            continue
        else:
            print("YOU MISS!")
            enemysheet.update_cell(user_guess[0], user_guess[1], 'x')
            break


def game(total_ships, enemysheet, playersheet):
    game_enemy_ships = total_ships
    game_player_ships = total_ships
    game_over = False
    player_guess_val = False
    enemy_guess_val = False

    while game_over is False:
        if player_guess_val is True:
            game_enemy_ships -= 1
            player_guess_val = False

        if enemy_guess_val is True:
            game_player_ships -= 1
            enemy_guess_val = False

        if game_enemy_ships == 0:
            print("You win!")
            game_over = True
            break
        else:
            player_guess_val = player_guess(enemysheet)

        if game_player_ships == 0:
            print("You Lose")
            game_over = True
            break
        else:
            enemy_guess_val = enemy_guess(playersheet)


def exit_game(sheet1, sheet2):
    SHEET.del_worksheet(sheet1)
    SHEET.del_worksheet(sheet2)


def main():
    total_ships = 3
    playersheet = initiate_player(total_ships)
    enemysheet = enemy_ship(total_ships)
    game(total_ships, enemysheet, playersheet)
    exit_game(enemysheet, playersheet)


main()
