# from dotenv import load_dotenv
import sqlite3


# Get DB connection
def get_db_connection(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
