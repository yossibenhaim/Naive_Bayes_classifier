from printer import Printer
from menu_router import MenuRouter

class Menu:

    @staticmethod
    def start_menu():
        stop_loop = True
        while stop_loop:
            Printer.start_menu()
            choice = input()
            if choice in MenuRouter.routes_start_nemu:
                return choice