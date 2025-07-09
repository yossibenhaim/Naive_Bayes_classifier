from printer import Printer

class Menu:

    @staticmethod
    def start_menu():
        Printer.start_menu()
        choice = input()
        return choice