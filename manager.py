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


        self.routes_start_nemu = {
            "1": lambda data: CheckProbability(self.data_dict,self.data).check(),
            "2": lambda daya: CheckProbability(self.data_dict,self.data).test(self.data),
            "3": self.create_new_data,
            "4": "exit",
        }

        self.routes_manager_nemu_add_data = {
            "1": self.print_data_frame,
            "2": lambda data: DataCleaning(data).change_index(),
            "3": lambda data: ModelTraining(self.data),
            "4": "exit",
        }

    def start(self):

        stop_loop = True
        while stop_loop:
            choice = Menu.start_menu()
            x = self.get_routes_start_nemu(choice)
            if x == "exit":
                Printer.exit()
                break
            if x:
                result = x(self.data)
                if isinstance(result, pandas.DataFrame):
                    self.data = result


    def create_new_data(self, data):
        self.data = DAL.reading_csv_file()
        self.menu_new_model()


    def menu_new_model(self):

        choice = ""
        while choice != "exit":
            Printer.menu_manager_model_traning()
            choice = input()
            x = self.get_routes_manager_nemu_add_data(choice)
            if x == "exit":
                Printer.exit()
                return
            if x:
                result = x(self.data)
                print("result =",result)
                if isinstance(result, pandas.DataFrame):
                    self.data = result
                if isinstance(result, ModelTraining):
                    self.data_dict = result.data_dict
            else:
                Printer.invalid_selection()

    def print_data_frame(self, data):
        print(self.data_dict)

    def print_data_dict(self, data):
        print(self.data_dict)



    def get_routes_start_nemu(self, choice):
        return self.routes_start_nemu.get(choice)

    def get_routes_manager_nemu_add_data(self, choice):
        return self.routes_manager_nemu_add_data.get(choice)

a = Manager()
a.start()
