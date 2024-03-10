import os
from food_manager.utils.constants import DB_PATH
from pathlib import Path
import json

def db_path() -> Path:
    """
    Returns the path to the database file

    Returns:
        Path: The path to the database file
    """
    ensure_db()
    return Path(DB_PATH)

def ensure_db() -> None:
    """
    Ensures that the database file exists.
    If the file doesn't exist, it creates an empty database file.

    Returns:
        None
    """
    if not Path(DB_PATH).exists():
        with open(Path(DB_PATH), "w") as file:
            file.write("[]")
            file.close()
    else:
        return
    
def get_length() -> int:
    """
    Returns the number of items in the database

    Returns:
        int: The number of items in the database
    """
    with open(db_path(), "r") as file:
        data = file.read()
        file.close()
    return len(data)

def get_data() -> dict:
    """
    Returns the data in the database

    Returns:
        list: The data in the database
    """
    with open(db_path(), "r") as file:
        data = json.load(file)
        file.close()
    return data