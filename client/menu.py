class Menu:

    def __init__(self, manager):
        """
        Initializes an instance of the Menu class with a given Manager instance.

        Args:
            manager (Manager): The Manager instance used to interact with data and the server.
        """
        self.Manager = manager

    def run_menu(self):
        """
        Runs the main menu loop:
        Allows the user to choose between viewing the DataFrame, checking probabilities,
        loading and processing a CSV file, or exiting the program.
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
        Displays the main menu options to the user.
        """
        print("\n--- Main Menu ---")
        print("1. View Data Frame")
        print("2. Check Probability (Train and Test Model)")
        print("3. Load and Process CSV")
        print("4. Exit")
        print("-----------------\n")
