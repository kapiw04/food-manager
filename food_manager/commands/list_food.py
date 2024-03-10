import json
from food_manager.utils.db import get_data
from food_manager.views.food_menu import FoodList

class ListFoodCommand:
    def run(self) -> int:
        """
        Executes the command to list food items and returns the chosen ID.

        Returns:
            int: The ID of the chosen food item.
        """
        chosen_id = FoodList(get_data()).show()
        return chosen_id

            