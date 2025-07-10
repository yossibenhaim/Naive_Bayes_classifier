class Printer:

    @staticmethod
    def start_suftuer():
        print("Welcome to the Naive Bayes Classifier Application")

    @staticmethod
    def start_menu():
        print("Main Menu:\n"
        "1 - Check probability\n"
        "2 - Test the classifier\n"
        "3 - Train a new model\n"
        "4 - Exit from program")

    @staticmethod
    def file_name_request():
        print("🔍 Enter the full file path to open (e.g., C:/Users/YourName/Desktop/data.csv):")

    @staticmethod
    def menu_manager_model_traning():
        print("Management Menu - Data Management\n"
        "1 - Print the new data\n"
        "2 - Clear the new table\n"
        "3 - Generate statistics on the new table\n"
        "4 - Exit")

    @staticmethod
    def invalid_selection():
        print("Invalid selection - please choose again")

    @staticmethod
    def exit():
        print("Goodbye! You have exited the program")

    @staticmethod
    def print_data_frame(data):
        print(data)

    @staticmethod
    def print_data_dict(data):
        print(data)


