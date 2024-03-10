from simple_term_menu import TerminalMenu
from food_manager.utils.styles import MENU_CURSOR, MENU_CURSOR_STYLE, MENU_HIGHLIGHT_STYLE
from food_manager.utils.settings import get_settings, save_setting

class SettingsMenu:
    def __init__(self):      
        self.options = [
            "Sort by",
            "Go back"
        ]
        self.menu = TerminalMenu(self.options, title="Settings", menu_cursor=MENU_CURSOR, menu_cursor_style=MENU_CURSOR_STYLE, menu_highlight_style=MENU_HIGHLIGHT_STYLE)
        self.sort_by_menu = SortByMenu()

    def show(self):
        self.menu.show()
        selected_option = self.menu.chosen_menu_index
        if selected_option == 0:
            return self.sort_by_menu.show()
        else:
            return
        
class SortByMenu:
    def __init__(self):      
        self.options = [
            "Expiration date",
            "Name",
            "Go back"
        ]
        self.menu = TerminalMenu(self.options, title="Sort by", menu_cursor=MENU_CURSOR, menu_cursor_style=MENU_CURSOR_STYLE, menu_highlight_style=MENU_HIGHLIGHT_STYLE)

    def show(self):
        self.menu.show()
        selected_option = self.menu.chosen_menu_index
        if selected_option == 0:
            self.handleChoice("expiration_date")
        elif selected_option == 1:
            self.handleChoice("name")
        else:
            return
        
    
    def handleChoice(self, choice):
        save_setting("sort_by", choice)
        return choice