from printer import Printer


class Menu:

    @staticmethod
    def start_menu():
        choice = input(Printer.start_menu())
        if choice == "1":
            pass