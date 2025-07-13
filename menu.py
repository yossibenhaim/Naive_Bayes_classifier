from manager import Manager

class Menu:

    def __init__(self, manager):
        self.Manager = manager

    def run_menu(self):
        stop_loop = True
        while stop_loop:
            self.print_menu()
            choice = input("send your choice\n")
            if choice == "1":
                self.Manager.load_csv()
            elif choice == "2":
                self.Manager.clean_data()
            elif choice == "3":
                self.Manager.create_probability()
            elif choice == "4":
                self.Manager.create_check_probability()
            elif choice == "5":
                stop_loop = False

    def print_menu(self):
        print("\nMenu:")
        print("1. Load CSV file")
        print("2. Clean data (choose index column)")
        print("3. Train classifier (Naive Bayes)")
        print("4. Test classification on new row")
        print("5. Exit\n")


manager = Manager()
a = Menu(manager)
a.run_menu()