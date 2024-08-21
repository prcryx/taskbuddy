# from dotenv import load_dotenv
import sqlite3
from taskbuddy.utils import get_default_db_path


class DatabaseConnectionFactory:
    @staticmethod
    def create_connection(db_type="sqlite"):
        if db_type == "sqlite":
            return sqlite3.connect(get_default_db_path())
        # Future extension for other databases can be added here
        raise ValueError(f"Unsupported database type: {db_type}")


# SQLite Adapter for connection handling
class SQLiteAdapter:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def execute(self, query, params=None):
        if params:
            return self.cursor.execute(query, params)
        return self.cursor.execute(query)

    def commit(self):
        self.connection.commit()

    def fetch_all(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
