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
        print(tries)
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
        print(enemysheet)
    return enemysheet


def initiate_player(total_ships):
    game_total_ships = 3
    playersheet = battle_sheet()
    while game_total_ships != 0:
        position = shoot("placement")
        print(position)
        guess_try = playersheet.cell(position[0],
                                     position[1]).value
        if guess_try is None:
            playersheet.update_cell(position[0], position[1], 'x')
            game_total_ships -= 1
        else:
            print("You have allready positioned a ship here, Try another one")
    return playersheet


def shoot(text):
    while True:
        try:
            guess_row = input(f"Make your {text}! \nRow: ")
            if int(guess_row) > 10 or int(guess_row) < 0:
                raise ValueError("number out of range")
            guess_col = input("Collumn: ")
            if int(guess_col) > 10 or int(guess_col) < 0:
                raise ValueError("number out of range")
            guessed_answered = [int(guess_row), int(guess_col)]
            break
        except ValueError as error:
            print(f"Unkown input:{error}")
            print("please provide a number between 1 and 10.")
    return guessed_answered


def game(total_ships, enemysheet):
    game_total_ships = total_ships
    while game_total_ships != 0:
        user_guess = shoot("guess")
        print(user_guess)
        guess_try = enemysheet.cell(user_guess[0],
                                    user_guess[1]).value
        if guess_try == "o":
            print("HIT!")
            game_total_ships -= 1
            print(f"{game_total_ships} left!")
            enemysheet.update_cell(user_guess[0], user_guess[1], 'x')
        elif guess_try == "":
            print("You allready fired upon this coordinates, try another one.")
        else:
            print("MISS!")
            enemysheet.update_cell(user_guess[0], user_guess[1], 'x')
    print("You win!")


def exit_game(sheet1, sheet2):
    SHEET.del_worksheet(sheet1)
    SHEET.del_worksheet(sheet2)


def main():
    total_ships = 3
    playersheet = initiate_player(total_ships)
    enemysheet = enemy_ship(total_ships)
    game(total_ships, enemysheet)
    exit_game(enemysheet, playersheet)


main()
