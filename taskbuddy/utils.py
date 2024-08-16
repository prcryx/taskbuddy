from datetime import datetime
from pathlib import Path
from typing import Union
from taskbuddy.constants import (
    ASSET_DIRNAME,
    ART_FILENAME,
    DD_MM_YYYY,
    DEFAULT_ART,
    DB_DIRNAME,
    SQLITE_DB_FILE,
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


# Get default db path
def get_default_db_path() -> str:
    return get_path(DB_DIRNAME, SQLITE_DB_FILE)


# Check if the file exists or not
def file_exists(dir_name: str, file_name: str) -> bool:
    project_path = Path.cwd()
    file_path = project_path / dir_name / file_name
    return file_path.exists()


# Parse the date in DD-MM-YYYY format
def parse_date_ddMMYYY(due_date: str) -> datetime:
    return datetime.strptime(due_date, DD_MM_YYYY)
