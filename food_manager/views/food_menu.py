from simple_term_menu import TerminalMenu
from food_manager.utils.styles import MENU_CURSOR, MENU_CURSOR_STYLE, MENU_HIGHLIGHT_STYLE
from food_manager.models.food import Food

# Format the food list
# f"{food['name']<

class FoodList:
    def __init__(self, data):
        self.data = data
        self.ids = [food['id'] for food in data]
        self.food_list = []
        for id in self.ids:
            self.food_list.append(self.get_food(id))
        self.options = [f"{food.name.center(30)} {(str(int(food.time_to_expire()))+' days').center(30)}" for food in self.food_list]
        self.options.append("")
        self.options.append("Go back")
        self.menu = TerminalMenu(self.options, title=f"{'Name'.center(30)} {'Expires in'.center(30)}", menu_cursor=MENU_CURSOR, menu_cursor_style=MENU_CURSOR_STYLE, menu_highlight_style=MENU_HIGHLIGHT_STYLE, cycle_cursor=False, skip_empty_entries=True)

    def show(self) -> int:
        self.menu.show()
        if self.menu.chosen_menu_index == len(self.options) - 1:
            return -1
        return self.ids[self.menu.chosen_menu_index]

    def get_food(self, id: int) -> Food:
        for food in self.data:
            if food['id'] == id:
                return Food(**food)
        return None
