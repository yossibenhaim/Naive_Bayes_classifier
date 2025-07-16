from client.manager import Manager


class Menu:

    def __init__(self, manager):
        """
        Initializes Menu with a Manager instance.

        Args:
            manager (Manager): The Manager instance to interact with.
        """
        self.Manager = manager

    def run_menu(self):
        """
        Main menu loop: lets user load CSV, go to manager menu or exit.
        """
        stop_loop = True
        while stop_loop:
            self.print_menu()
            choice = input("send your choice\n")
            if choice == "1":
                self.Manager.load_csv_and_process()
            elif choice == "2":
                self.run_menu_manager()
            elif choice == "3":
                stop_loop = False

    def run_menu_manager(self):
        """
        Manager submenu loop: allows data printing, cleaning, training, testing, checking, or exit.
        """
        stop_loop = True
        while stop_loop:
            self.print_menu_manager()
            choice = input("send your choice\n")
            if choice == "1":
                print(self.Manager.return_data_frame())
            elif choice == "2":
                self.Manager.clean_data()
            elif choice == "3":
                self.Manager.create_probability()
            elif choice == "4":
                self.Manager.test_probability()
            elif choice == "5":
                self.Manager.check_probability()
            elif choice == "6":
                stop_loop = False

    def print_menu(self):
        """
        Prints main menu options.
        """
        print("\nMenu:")
        print("1. Load CSV file")
        print("2. manager menu")
        print("3. exit\n")

    def print_menu_manager(self):
        """
        Prints manager submenu options.
        """
        print("\nMenu:")
        print("1. Print CSV file")
        print("2. Clean data (choose index column)")
        print("3. Train classifier (Naive Bayes)")
        print("4. Test classification on new row")
        print("5. Check classification on new row")
        print("6. Exit\n")


manager = Manager()
a = Menu(manager)
a.run_menu()
