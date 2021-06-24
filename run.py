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
    check_available_sheet = False
    while check_available_sheet is False and tries > 0:
        try:
            sheet_number = str(random.randint(1, 1))
            battlesheet = SHEET.add_worksheet(title=sheet_number,
                                              rows="10", cols="10")
            check_available_sheet = True
        except Exception:
            if tries > 5:
                tries += 1
            else:
                print("No battlesheet available! please try again later.")
                quit()
    return battlesheet


def enemy_ship():
    enemysheet = battle_sheet()
    number_of_ships = 0
    while number_of_ships < 3:
        enemy_ship_row = random.randint(1, 10)
        enemy_ship_col = random.randint(1, 10)
        enemy_ship_pos = [enemy_ship_row, enemy_ship_col]
        enemysheet.update_cell(enemy_ship_pos[0],
                            enemy_ship_pos[1], 'x')
        number_of_ships += 1
        print(enemysheet)
    return enemysheet


def guess():
    guess_row = input("Make your guess! \nRow: ")
    guess_col = input("Collumn: ")
    guessed_answered = [int(guess_row), int(guess_col)]
    return guessed_answered


def game():
    enemy_ship_pos = enemy_ship()
    if enemy_ship_pos == guess():
        print("HIT!")
    else:
        print(f"MISS! enemy ship was at {enemy_ship_pos}")


def main():
    enemysheet = enemy_ship()
    Check_if_sheet_exists = input("succes: ")
    print(Check_if_sheet_exists)
    SHEET.del_worksheet(enemysheet)


main()
