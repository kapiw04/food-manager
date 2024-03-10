import os
import sys
import json
from food_manager.utils.db import db_path, get_length
from food_manager.utils.date import fill_date

class AddCommand:
    def run(self):
        id = get_length() + 1
        name = input("Enter the name of the food: ")
        expiration_date = fill_date(input("Enter the expiration date (DD-MM-YYYY): "))
        quantity = input("Enter the quantity: ")
        opened = input("Is the food opened? (y/n): ")
        opened_date = fill_date(input("Enter the date when the food was opened (DD-MM-YYYY): "))

        food = {
            "id": id,
            "name": name,
            "expiration_date": expiration_date,
            "quantity": quantity,
            "opened": True if opened.lower() in ["y", "yes", "yse", "ye"] else False,
            "opened_date": opened_date
        }

        with open(db_path(), "r") as file:
            data = json.load(file)
            data.append(food)
            file.close()

        with open(db_path(), "w") as file:
            json.dump(data, file)
            file.close()
        print("Food added successfully!")
