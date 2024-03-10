from food_manager.views import main_menu, food_menu
from food_manager.utils.db import ensure_db

if __name__ == "__main__":
    ensure_db()
    main_menu = main_menu.MainMenu()
    main_menu.show()

