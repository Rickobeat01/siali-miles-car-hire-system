import sqlite3
import os

DB_FILE = "database/carhire.db"

def initialize_database():
    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)

    conn.commit()
    conn.close()

if name == "main":
    initialize_database()
    print("Database created successfully.")
