from simple_term_menu import TerminalMenu
from food_manager.commands.commands import Add, Remove, ListFood
from food_manager.utils.styles import MENU_CURSOR, MENU_CURSOR_STYLE, MENU_HIGHLIGHT_STYLE
from food_manager.utils.db import get_data
from food_manager.views import food_menu, settings_menu

class MainMenu:
    def __init__(self):      
        self.options = [
            "Add food",
            "List all food",
            "Remove food",
            "Update food (coming soon)",
            "Settings",
            "Exit"
        ]
        self.mainMenu = TerminalMenu(self.options, title="Main Menu", menu_cursor=MENU_CURSOR, menu_cursor_style=MENU_CURSOR_STYLE, menu_highlight_style=MENU_HIGHLIGHT_STYLE)
        self.food_menu = food_menu.FoodList(get_data())
        self.settings_menu = settings_menu.SettingsMenu()

    def show(self):
        self.mainMenu.show()
        selected_option = self.mainMenu.chosen_menu_index
        if selected_option == 0:
            Add.run()
        elif selected_option == 1:
            chosen_food_id = ListFood.run()
            if chosen_food_id == -1:
                self.show()
        elif selected_option == 2:
            chosen_food_id = food_menu.show()
            if chosen_food_id != -1:
                Remove.run(chosen_food_id)
            else:
                self.show()
        # elif selected_option == 3:
        #     Update().run()
        elif selected_option == 4:
            choice = self.settings_menu.show()
            if choice:
                self.settings_menu.handleChoice(choice)       
            self.show()     
        else:
            print("Goodbye!")
            exit(0)