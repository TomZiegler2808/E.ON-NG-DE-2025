import sqlite3

conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
""")

conn.commit()
conn.close()
print("SQLite database 'notes.db' initialized with table 'notes'.")