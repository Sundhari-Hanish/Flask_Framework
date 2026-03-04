import sqlite3
con = sqlite3.connect("event.db")
con.execute("""CREATE TABLE participants(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    domain TEXT NOT NULL)""")
print("Database created successfully!")
con.close()
