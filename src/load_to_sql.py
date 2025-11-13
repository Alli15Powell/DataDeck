import pandas as pd
import sqlite3
import os

DB_PATH = "data/datadeck.db"
CSV_PATH = "data/cleaned/steam_cleaned.csv"

# Make sure the file exists before loading
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"Could not find {CSV_PATH}")

# Connect to (or create) the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS games (
    appid INTEGER PRIMARY KEY,
    name TEXT,
    release_date TEXT,
    developer TEXT,
    publisher TEXT,
    platforms TEXT,
    required_age INTEGER,
    categories TEXT,
    genres TEXT,
    positive_ratings INTEGER,
    negative_ratings INTEGER,
    price REAL
);
""")

# Load the cleaned CSV
df = pd.read_csv(CSV_PATH)

# Insert data into SQL table
df.to_sql("games", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Data successfully loaded into datadeck.db!")
