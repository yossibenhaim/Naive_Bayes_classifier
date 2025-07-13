
class Menu:

    def __init__(self, manager):
        self.manager = manager

    def run_menu(self):
        stop_loop = True
        while stop_loop:
            choice = input("send your choice\n")
            if choice == "1":
                self.manager.load_csv()
            if choice == "2":
                pass
            if choice == "3":
                self.manager.create_probability()
            if choice == "4":
                stop_loop = False
