from math import exp
import sqlite3
from datetime import date, datetime, timedelta
import random

while True:
    with sqlite3.connect('backend.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM tokens')
        tokens = cursor.fetchall()
        db.commit()

    today = datetime.now()

    print("Tokens:")
    print(tokens)

    print("""1.  Generate New Token.
          2.  Update Token.
          3.  Delete Token.""")
    user_input = input("Action: ")
    if user_input == "1":
        for i in range(10):
            token = random.randint(0, 9)
        perm_lvl = input(
            "What perm level do you want the token to hold? (1/2): ")
        print("""Expirery options:
              1.  1 Day.
              2.  7 Days.
              3.  No Expirery.""")
        exp_period = input("Choose an Option: ")
        print("NEW TOKEN GENERATED!")
        print(f"TOKEN: {token}")
        print(f"PERM LEVEL: {perm_lvl}")

        if exp_period == '1':
            exp_date = today + timedelta(1)
            sql = 'INSERT INTO tokens (token, perm_level, expires) VALUES (%s, %s, %s)'
            print(f"Expirery Date: {exp_period} - {exp_date}")
            vals = (token, perm_lvl, exp_date)
        elif exp_period == '2':
            exp_date = today + timedelta(7)
            sql = 'INSERT INTO tokens (token, perm_level, expires) VALUES (%s, %s, %s)'
            print(f"Expirery Date: {exp_period} - {exp_date}")
            vals = (token, perm_lvl, exp_date)
        else:
            sql = 'INSERT INTO tokens (token, perm_level) VALUES (%s, %s)'
            print(f"Expirery Date: NO-EXPIRERY")
            vals = (token, perm_lvl)

        with sqlite3.connect('backend.db') as db:
            cursor = db.cursor()
            cursor.execute(sql, vals)
            db.commit()
