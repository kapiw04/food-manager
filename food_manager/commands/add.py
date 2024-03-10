import os
import sys
import json
from food_manager.utils.db import get_length, get_data
from food_manager.utils.date import fill_date
from food_manager.utils.settings import get_setting

class AddCommand:
    def run(self):
        id = get_length() + 1
        name = input("Enter the name of the food: ")
        expiration_date = fill_date(input("Enter the expiration date (DD-MM-YYYY): "))
        quantity = input("Enter the quantity: ")
        opened = input("Is the food opened? (y/n): ")
        opened = True if opened.lower() in ["y", "yes", "yse", "ye"] else False
        if opened:
            opened_date = fill_date(input("Enter the date when the food was opened (DD-MM-YYYY): "))
        else:
            opened_date = None

        food = {
            "id": id,
            "name": name,
            "expiration_date": expiration_date,
            "quantity": quantity,
            "opened": opened,
            "opened_date": opened_date
        }
        
        self.insert_food(food)
        
        print("Food added successfully!")

    def insert_food(self, food):
        sort_by = get_setting("sort_by")
        data = get_data()

        for i in range(len(data)):
            if data[i][sort_by] > food[sort_by]:
                data.insert(i, food)
                break