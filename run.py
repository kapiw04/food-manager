from food_manager.views import main_menu, food_menu
from food_manager.utils.db import ensure_db
from food_manager.utils.settings import ensure_settings

if __name__ == "__main__":
    ensure_db()
    ensure_settings()
    main_menu = main_menu.MainMenu()
    main_menu.show()

