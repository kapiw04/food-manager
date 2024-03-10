from simple_term_menu import TerminalMenu
from food_manager.utils.styles import MENU_CURSOR, MENU_CURSOR_STYLE, MENU_HIGHLIGHT_STYLE

class FoodList:
    def __init__(self, data):
        self.data = data
        self.options = [f"{food['name']} - {food['expiration_date']}" for food in data]
        self.ids = [food['id'] for food in data]
        self.options.append("Go back")
        self.menu = TerminalMenu(self.options, title="Food List", menu_cursor=MENU_CURSOR, menu_cursor_style=MENU_CURSOR_STYLE, menu_highlight_style=MENU_HIGHLIGHT_STYLE)

    def show(self) -> int:
        self.menu.show()
        if self.menu.chosen_menu_index == len(self.options) - 1:
            return -1
        return self.ids[self.menu.chosen_menu_index]
