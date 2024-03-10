import json
from pathlib import Path
from food_manager.utils.constants import SETTINGS_PATH

def get_settings() -> dict:
    """
    Returns the settings from the settings file

    Returns:
        dict: The settings from the settings file
    """
    with open(SETTINGS_PATH, "r") as file:
        data = json.load(file)
        file.close()
    return data

def save_settings(data: dict) -> None:
    """
    Saves the settings to the settings file

    Args:
        data (dict): The settings to be saved

    Returns:
        None
    """
    with open(SETTINGS_PATH, "w") as file:
        json.dump(data, file)
        file.close()
    return

def get_setting(key: str) -> str:
    """
    Returns the value of a specific setting

    Args:
        key (str): The key of the setting to be returned

    Returns:
        str: The value of the setting
    """
    settings = get_settings()
    return settings[key]

def save_setting(key: str, value: str) -> None:
    """
    Saves a setting to the settings file

    Args:
        key (str): The key of the setting to be saved
        value (str): The value of the setting to be saved

    Returns:
        None
    """
    settings = get_settings()
    settings[key] = value
    save_settings(settings)
    return

def get_settings_path() -> Path:
    """
    Returns the path to the settings file

    Returns:
        Path: The path to the settings file
    """
    return Path(SETTINGS_PATH)

def ensure_settings() -> None:
    """
    Ensures that the settings file exists.
    If the file doesn't exist, it creates an empty settings file.

    Returns:
        None
    """
    settings_template = {
        "sort_by": "expiration_date",
    }
    if not Path(SETTINGS_PATH).exists():
        with open(Path(SETTINGS_PATH), "w") as file:
            file.write(json.dumps(settings_template))
            file.close()
    else:
        return
    return