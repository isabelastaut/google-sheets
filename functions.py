import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)

sh = client.open("Habit Tracker 2021")
sheet = sh.get_worksheet(0)
habit_sheet = sh.get_worksheet(1)


def get_month_name(month):
    row = 2 + (10 * (int(month) - 1))
    month_name = sheet.cell(row, 9).value
    return month_name


def get_habits():
    row = 3
    column = 2

    print("Your current habits are:")
    for habit in range(6):
        print(f'   [{habit + 1}] {habit_sheet.cell(row, column).value}')
        row += 1


def set_habits():
    row = 3
    column = 2

    print("Your current habits are:")
    for habit in range(6):
        print(f'   [{habit + 1}] {habit_sheet.cell(row, column).value}')
        row += 1

    print('-'*52)
    habit_number = int(input('Select the number of the habit you want to change: '))
    new_habit = input('Type your new habit: ')

    print(f"Changing the habit '{habit_sheet.cell((habit_number + 2), 2).value}' for '{new_habit}'...")
    habit_sheet.update_cell((habit_number + 2), 2, new_habit)
    print('Done!')


def fill_habits(month, day):
    column = int(day) + 9
    row = 4 + (10 * (int(month) - 1))
    month_name = get_month_name(month)

    print(f'On {month_name} {day}th, did you:')
    for habit in range(6):
        answer = input(f'{sheet.cell(row, 9).value}? (y/n) ')
        if answer.strip().lower() == 'y':
            sheet.update_cell(row, column, True)
        else:
            sheet.update_cell(row, column, False)

        row += 1


def check_month(month):
    row = 4 + (10 * (int(month) - 1))
    month_name = get_month_name(month)
    print(f'During the month of {month_name} you did...')
    for habit in range(6):
        print(f'   - {sheet.cell(row, 9).value}: {sheet.cell(row, 41).value} times.')
        row += 1
