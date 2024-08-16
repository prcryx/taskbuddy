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
    def __init__(self, connection):
        self.connection = connection

    def execute(self, query, params=None):
        with self.connection:
            if params:
                return self.connection.execute(query, params)
            return self.connection.execute(query)

    def close(self):
        self.connection.close()
