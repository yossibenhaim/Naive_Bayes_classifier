class Printer:

    @staticmethod
    def start_suftuer():
        print("Welcome to the Naive Bayes Classifier Application")

    @staticmethod
    def start_menu():
        print("Main Menu:\n"
        "1 - Check probability\n"
        "2 - Test the classifier\n"
        "3 - Train a new model\n")

    @staticmethod
    def file_name_request():
        print("🔍 Enter the full file path to open (e.g., C:/Users/YourName/Desktop/data.csv):")

    @staticmethod
    def menu_manager_model_traning():
        print("Admin Menu - Manage Data\n"
              "1 - Print new data\n"
              "2 - Clear existing data \n"
              "3 - Exit")

    @staticmethod
    def invalid_selection():
        print("Invalid selection - please choose again")