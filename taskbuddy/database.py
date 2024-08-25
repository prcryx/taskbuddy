# from dotenv import load_dotenv
import sqlite3
from taskbuddy.utils import get_db_path, get_migration_status_file


class DatabaseConnectionFactory:
    @staticmethod
    def create_connection(db_type="sqlite"):
        if db_type == "sqlite":
            try:
                status_file = get_migration_status_file()
                with open(status_file, "r") as f:
                    file_name = f.read()
                    f.close()
            except FileNotFoundError:
                file_name = None
            return sqlite3.connect(get_db_path(file_name))
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
