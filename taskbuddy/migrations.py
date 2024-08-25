import os.path
import sqlite3
import click
from taskbuddy.constants import (
    SQL_MIGRATION_DIRNAME,
)
from taskbuddy.utils import (
    get_path,
    get_db_path,
    db_status_file_exists,
    get_migration_status_file,
)


def run_migration(db_name: str = None):
    """Run SQL migrations from the sql/ directory."""
    if db_status_file_exists():
        return

    # Connect to SQLite database
    # db_path = get_default_db_path() if db_path is None else db_path
    db_path = get_db_path(db_name)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Run SQL files from the sql/ directory
    sql_dir = get_path(SQL_MIGRATION_DIRNAME, to_string=False)
    sql_files = sorted(f for f in sql_dir.glob("**/*.sql") if f.is_file())
    for filename in sql_files:
        file_path = str(sql_dir / filename)
        with open(file_path, "r") as sql_file:
            sql_script = sql_file.read()
            cursor.executescript(sql_script)
            sql_file.close()
            click.echo(f"Executed migration: {filename}")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    # Mark the migration as done
    status_file_path = get_migration_status_file()
    dbname = os.path.basename(db_path)
    with open(status_file_path, "w") as f:
        f.write(dbname)
        f.close()

    click.echo("[200|Ok]: Migrations completed successfully.")
