from food_manager.utils.db import db_path, get_data
import json
from food_manager.views.food_menu import FoodList

class ListFoodCommand:
    def __init__(self) -> None:
        self.food_list = FoodList(get_data())
    def run(self) -> int:
            """
            Executes the command to list food items and returns the chosen ID.

            Returns:
                int: The ID of the chosen food item.
            """
            chosen_id = self.food_list.show()
            return chosen_id

    def sort_data(self, data) -> list:
        """
        Sorts the data by expiration date

        Args:
            data (list): The data to be sorted

        Returns:
            list: The sorted data
        """
        return sorted(data, key=lambda k: k['expiration_date'])
            