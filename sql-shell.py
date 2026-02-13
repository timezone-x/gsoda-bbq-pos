import sqlite3

user_input = input("what file would you like to open? ")

db = sqlite3.connect(user_input)
cursor = db.cursor()

while True:
    user_input = input("please enter an SQL command: ")
    try:
        cursor.execute(user_input)
        print(cursor.fetchall())
    except:
        print("An error ocurred")
