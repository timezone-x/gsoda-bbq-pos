import sqlite3

db = sqlite3.connect("BBQ-POS.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE "transaction" (
               "id" int PRIMARY KEY,
               "datetime" datetime NOT NULL,
               "with" int NOT NULL,
               "without" int NOT NULL,
               "drinks" int NOT NULL,
               "donation" int,
               "total" int NOT NULL)""")

db.commit()
