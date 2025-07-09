from printer import Printer
from menu_router import MenuRouter

class Menu:

    @staticmethod
    def start_menu():
        Printer.start_menu()
        choice = input()
        x = MenuRouter.get_routes_start_nemu(choice)
        if x:
            x()
        else:
            Printer.invalid_selection()
Menu.start_menu()