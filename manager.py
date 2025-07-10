import pandas
from model_traning.DAL import DAL
from printer import Printer
from menu import Menu
from model_traning.model_training import ModelTraining
from model_traning.data_cleaning import DataCleaning
from check_probability import CheckProbability

class Manager:

    def __init__(self):
        self.data = None
        self.data_dict = None
        self.routes_start_menu = {
            "1": self.run_check,
            "2": self.run_test,
            "3": self.create_new_data,
            "4": "exit",
        }
        self.routes_manager_menu_add_data = {
            "1": Printer.print_data_frame,
            "2": lambda data: DataCleaning(data).change_index(),
            "3": lambda data: ModelTraining(self.data),
            "4": "exit",
        }

    def start(self):
        stop_loop = True
        while stop_loop:
            choice = Menu.start_menu()
            action  = self.get_routes_start_menu(choice)
            if action  == "exit":
                Printer.exit()
                break
            if action :
                result = action()
                if isinstance(result, pandas.DataFrame):
                    self.data = result
                if isinstance(result, ModelTraining):
                    self.data_dict = result


    def create_new_data(self):
        self.data = DAL.reading_csv_file()
        self.menu_new_model()


    def menu_new_model(self):
        choice = ""
        while choice != "exit":
            Printer.menu_manager_model_traning()
            choice = input()
            action  = self.get_routes_manager_menu_add_data(choice)
            if action  == "exit":
                Printer.exit()
                return
            if action :
                result = action (self.data)
                print("result =",result)
                if isinstance(result, pandas.DataFrame):
                    self.data = result
                if isinstance(result, ModelTraining):
                    self.data_dict = result.data_dict
            else:
                Printer.invalid_selection()


    def get_routes_start_menu(self, choice):
        return self.routes_start_menu.get(choice)


    def get_routes_manager_menu_add_data(self, choice):
        return self.routes_manager_menu_add_data.get(choice)


    def run_check(self):
        if self.data_dict is None:
            print("⚠️ Error: Please train the model first (option 3).")
            return
        return CheckProbability(self.data_dict, self.data).check(self.data)

    def run_test(self):
        if self.data_dict is None:
            print("⚠️ Error: Please train the model first (option 3).")
            return
        return CheckProbability(self.data_dict,self.data).test(self.data)


a = Manager()
a.start()
