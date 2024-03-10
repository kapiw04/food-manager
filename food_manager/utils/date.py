import time

def fill_date(input_date: str) -> str:
    """
    Fill the date with the current year and month if it's not present

    Args:
        input_date (str): The input date
    
    Returns:
        str: The date with the current year and month

    Example:
        fill_date("01-01") -> "01-01-2024"
    """
    separators = ["-", "/", "."]
    for separator in separators:
        if separator in input_date:
            date = input_date.split(separator)
            break
    else:
        date = input_date.split()

    if len(date) == 0:
        return f"{time.strftime('%d')}-{time.strftime('%m')}-{time.strftime('%Y')}"
    if len(date) == 1:
        return f"{date[0]}-{time.strftime('%m')}-{time.strftime('%Y')}"
    elif len(date) == 2:
        return f"{date[0]}-{date[1]}-{time.strftime('%Y')}"
    else:
        return input_date



