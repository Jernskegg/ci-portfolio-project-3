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
    sheet_number = str(random.randint(1, 10))
    newsheet = SHEET.add_worksheet(title=sheet_number, rows="10", cols="10")
    Check_if_sheet_exists = input("succes: ")
    SHEET.del_worksheet(newsheet)


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


battle_sheet()

# game()
