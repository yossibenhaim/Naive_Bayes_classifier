import logging
from client.manager import Manager, client_logger


class Menu:

    def __init__(self, manager):
        """
        Initializes the Menu with a Manager instance.

        Args:
            manager (Manager): Instance used for data operations.
        """
        self.Manager = manager

    def run_menu(self):
        """
        Runs the main menu loop.
        """
        stop_loop = True
        client_logger.info("Main menu loop started")
        while stop_loop:
            self.print_menu()
            choice = input("send your choice\n")
            client_logger.info(f"User selected option: {choice}")
            if choice == "1":
                client_logger.info("Displaying DataFrame")
                print(self.Manager.return_data_frame())
            elif choice == "2":
                client_logger.info("Initiating probability check")
                self.Manager.check_probability()
            elif choice == "3":
                client_logger.info("Loading and processing CSV")
                self.Manager.load_csv_and_process()
            elif choice == "4":
                client_logger.info("Exiting main menu loop")
                stop_loop = False
            else:
                client_logger.warning(f"Invalid choice: {choice}")

    def print_menu(self):
        """
        Prints the main menu.
        """
        print("\n--- Main Menu ---")
        print("1. View Data Frame")
        print("2. Check Probability (Train and Test Model)")
        print("3. Load and Process CSV")
        print("4. Exit")
        print("-----------------\n")


manager = Manager()
menu = Menu(manager)
menu.run_menu()
