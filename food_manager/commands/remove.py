from food_manager.utils.db import db_path
import json

class RemoveCommand:
    def run(self, food_id):
        with open(db_path(), "r") as file:
            data = json.load(file)
            file.close()

        for food in data:
            if food["id"] == food_id:
                data.remove(food)
                break

        with open(db_path(), "w") as file:
            json.dump(data, file)
            file.close()
        print("Food removed successfully!")