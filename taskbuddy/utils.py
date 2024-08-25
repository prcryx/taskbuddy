from datetime import datetime
from pathlib import Path
from typing import Union
from dateutil import parser

from taskbuddy.constants import (
    ASSET_DIRNAME,
    ART_FILENAME,
    DEFAULT_ART,
    DB_DIRNAME,
    SQLITE_DB_FILE,
    DD_MM_YYYY_HH_MM,
    MIGRATION_STATUS_FILENAME,
)


# Print header
def print_header() -> str:
    ascii_art_path = get_path(ASSET_DIRNAME, ART_FILENAME)
    try:
        with open(ascii_art_path, "r") as file:
            ascii_art = file.read()
    except FileNotFoundError:
        ascii_art = DEFAULT_ART

    return ascii_art


# Get dir or file path
def get_path(
    dir_name: str, file_name: str = None, to_string: bool = True
) -> Union[str, Path]:
    path = Path.cwd() / dir_name

    # Create the directory if it doesn't exist
    path.mkdir(parents=True, exist_ok=True)

    if file_name:
        path = path / file_name

    return str(path) if to_string else path


# Check for db
def isa_db(file_name: str) -> bool:
    return file_name.endswith(".db")


# Get default db path
def get_db_path(db_name: str = None) -> str:
    if db_name is not None and not isa_db(db_name):
        raise ValueError(f"{db_name} is not a database")
    if db_name is None:
        db_name = SQLITE_DB_FILE
    return get_path(DB_DIRNAME, db_name)


# Get migration status path
def get_migration_status_file() -> str:
    return get_path(DB_DIRNAME, MIGRATION_STATUS_FILENAME)


# Check if the file exists or not
def file_exists(dir_name: str, file_name: str) -> bool:
    project_path = Path.cwd()
    file_path = project_path / dir_name / file_name
    return file_path.exists()


# Check if MIGRATION_STATUS_FILE exists or not
def db_status_file_exists() -> bool:
    return file_exists(DB_DIRNAME, MIGRATION_STATUS_FILENAME)


# Parse and format the date in DD-MM-YYYY HH:MM format
def to_datestr(date_str: str) -> str:
    try:
        # Parse the time string into a datetime object
        parsed_time = parser.parse(date_str)
        # Format the datetime object to [dd-mm-yyyy HH:MM] str
        return parsed_time.strftime(DD_MM_YYYY_HH_MM)
    except parser.ParserError as e:
        raise ValueError(f"Could not parse the time string: {date_str}") from e


def parse_to_datetime(date_str: str) -> datetime:
    try:
        dt_obj = parser.parse(date_str)
        return dt_obj
    except parser.ParserError as e:
        raise ValueError(f"Could not parse the time string: {date_str}") from e
