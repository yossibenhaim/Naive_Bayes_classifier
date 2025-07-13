from manager import Manager

class Menu:

    def __init__(self, manager):
        self.Manager = manager

    def run_menu(self):
        stop_loop = True
        while stop_loop:
            choice = input("send your choice\n")
            if choice == "1":
                self.Manager.load_csv()
            elif choice == "2":
                self.Manager.clean_data()
            elif choice == "3":
                self.Manager.create_probability()
            elif choice == "4":
                stop_loop = False

manager = Manager()
a = Menu(manager)
a.run_menu()