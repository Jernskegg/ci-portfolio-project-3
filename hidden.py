"""
Import
"""
import sys
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

sh1 = SHEET.worksheet("TEST")
sh2 = SHEET.worksheet("TEST2")


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


print("TRUE "*10)
print("▼    "*10)
table(sh1, True)
print()
print("FALSE "*10)
print("▼    "*10)
table(sh2, False)
