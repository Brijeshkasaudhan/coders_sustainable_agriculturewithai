import sqlite3
from utils.logger import log_info, log_error

DB_NAME = "database/sustainable_farming.db"

def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        with open("database/schema.sql", "r") as f:
            cursor.executescript(f.read())

        conn.commit()
        conn.close()
        log_info("Database initialized ✅")
    except Exception as e:
        log_error(f"Error initializing database: {e}")

def insert_data(table, data):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table} VALUES ({placeholders})"
        cursor.execute(query, data)

        conn.commit()
        conn.close()
        log_info(f"Data inserted into {table} ✅")
    except Exception as e:
        log_error(f"Error inserting data into {table}: {e}")

def fetch_data(query):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        log_info(f"Data fetched successfully ✅")
        return results
    except Exception as e:
        log_error(f"Error fetching data: {e}")
        return []

