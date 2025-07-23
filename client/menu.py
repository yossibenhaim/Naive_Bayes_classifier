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
                print(self.Manager.return_data_frame())
            elif choice == "2":
                self.Manager.check_probability()
            elif choice == "3":
                self.Manager.load_csv_and_process()
            elif choice == "4":
                stop_loop = False

    def print_menu(self):
        """
        Prints the main menu options to the console.
        """
        print("\n--- Main Menu ---")
        print("1. View Data Frame")
        print("2. Check Probability (Train and Test Model)")
        print("3. Load and Process CSV")
        print("4. Exit")
        print("-----------------\n")


manager = Manager()
a = Menu(manager)
a.run_menu()
