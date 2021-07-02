"""
Import
"""
import sys
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
ADMIN_URL = "https://forms.gle/9mXCHJ2tEUNvyQyz8"
# Testing if Creds are valid
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
try:
    SHEET = GSPREAD_CLIENT.open('PROJECT3GAME')
except gspread.exceptions.SpreadsheetNotFound:
    print(f"""A fancy unexpected error occured
Please contact the admin on
"{ADMIN_URL}"
and tell the spreadsheet is missing""")
    sys.exit()
# end of authoratization


def battle_sheet():
    """
    Function creates a 10x10 cell worksheet
    and checks if sheets are not used by other users.
    """
    tries = 5
    while tries > 0:
        try:
            battlesheet = SHEET.duplicate_sheet(0,
                                                new_sheet_name=str(random.
                                                                   randint(1,
                                                                           10)
                                                                   )
                                                )
            break
        except gspread.exceptions.APIError:
            if tries > 1:
                tries -= 1
            else:
                print(f"""No battlesheet available! please try again later.
If this keeps happening, please contact {ADMIN_URL}""")
                sys.exit()
    return battlesheet


def table(sheet, hidden):
    """
    Shows a table in the console.
    """
    def fixed_length(text, length):
        if len(text) > length:
            text = text[:length]
        elif len(text) < length:
            text = (text + " " * length)[:length]
        return text
    tablesheet = sheet.get_all_values()
    if hidden is True:
        for step_1, x in enumerate(tablesheet):
            for step_2, a in enumerate(x):
                if "o" in a:
                    tablesheet[step_1][step_2] = a.replace("o", " ")

    row_number = 1
    print("0__|_1_|_2_|_3_|_4_|_5_|_6_|_7_|_8_|_9_|_10|")
    for row in tablesheet:
        val_print = f"{row_number}__"[:3]
        print(val_print, end="|")
        row_number += 1
        for collumn in row:
            print(end="_")
            print(fixed_length(collumn, 1), end="_|")
        print()


def enemy_ship(total_ships):
    """
    This initilizes the poisitioning of the computer controlled player
    """
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
    """
    This Function allows the user to input their ships to the battle sheet
    """
    game_enemy_ships = total_ships
    playersheet = battle_sheet()
    while game_enemy_ships != 0:
        table(playersheet, False)
        position = shoot("placement")
        print(position)
        guess_try = playersheet.cell(position[0],
                                     position[1]).value
        if guess_try is None or guess_try == " ":
            playersheet.update_cell(position[0], position[1], 'o')
            game_enemy_ships -= 1
        else:
            print("You have allready positioned a ship here, Try another one")
    return playersheet


def shoot(text):
    """
    This function allows the user to make a guess and validates it to confine
    it to a number between 1 to 10,
    and returns an error to the user, So that the user can try again.
    """
    while True:
        try:
            print(f"Make your {text}!")
            print("Row:")
            guess_row = input("")
            if int(guess_row) > 10 or int(guess_row) < 1:
                raise ValueError("number out of range")
            print("Collumn:")
            guess_col = input("")
            if int(guess_col) > 10 or int(guess_col) < 1:
                raise ValueError("number out of range")
            guessed_answered = [int(guess_row), int(guess_col)]
            break
        except ValueError as error:
            print(f"Unkown input:{error}")
            print("please provide a number between 1 and 10.")
    return guessed_answered


def enemy_guess(playersheet):
    """
    This function calls the Computer to make a random guess.
    It will return a "True"
    if the computer guess matches with the players ship on the worksheet
    """
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
        if guess_try == "x":
            continue
        print(f"enemy guessed {computer_guess}")
        print("ENEMY MISSED!")
        playersheet.update_cell(computer_guess[0], computer_guess[1], 'x')
        break


def player_guess(enemysheet):
    """
    This function takes the users input and compares it to the enemy worksheet
    to see if the guess corresponds to the sheet with eiter returning
    "None, X(Previous hit), o(Enemy ship)
    It will return a "True"
    if the user guess matches with an enemy ship on the worksheet
    """
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
        if guess_try == "x":
            print("You allready fired upon this coordinates, try another one.")
            continue
        print("YOU MISS!")
        enemysheet.update_cell(user_guess[0], user_guess[1], 'x')
        break


def game(total_ships, enemysheet, playersheet):
    """
    This function compares the values from total ships and reduces
    """
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
        table(enemysheet, True)
        player_guess_val = player_guess(enemysheet)
        if game_player_ships == 0:
            print("You Lose")
            game_over = True
            break
        table(playersheet, False)
        enemy_guess_val = enemy_guess(playersheet)


def exit_game(sheet1, sheet2):
    """
    cleans up the worksheets to make them available for other users.
    """
    SHEET.del_worksheet(sheet1)
    SHEET.del_worksheet(sheet2)


def main():
    """
    Main part of the application
    """
    total_ships = 3
    playersheet = initiate_player(total_ships)
    enemysheet = enemy_ship(total_ships)
    game(total_ships, enemysheet, playersheet)
    exit_game(enemysheet, playersheet)


main()
