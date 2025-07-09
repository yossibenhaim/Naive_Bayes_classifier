from model_traning.DAL import DAL
from printer import Printer
from menu import Menu
# from menu_router import MenuRouter
from model_traning.model_training import  ModelTraining
from model_traning.data_cleaning import DataCleaning

class Manager:

    def __init__(self):
        self.data = None
        self.data_dict = None


        self.routes_start_nemu = {
            "1": "1",
            "2": "2",
            "3": "create_new_data",
            "4": "exit",
        }

        self.routes_manager_nemu_add_data = {
            "1": self.print_data_frame,
            "2": lambda data: DataCleaning(data).change_index(),
            "3": lambda data: ModelTraining(data).return_data_dict,
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
            getattr(self,x)(self.data)


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
                if result:
                    self.data_dict = result()
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
