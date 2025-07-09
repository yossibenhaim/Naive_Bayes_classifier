from menu_router import MenuRouter
from model_traning.DAL import DAL
from printer import Printer
from menu import Menu


class Manager:

    def __init__(self):
        self.data = None


    def start(self):
        stop_loop = True
        while stop_loop:
            choice = Menu.start_menu()
            x = MenuRouter.get_routes_start_nemu(choice)
            if x == "exit":
                Printer.exit()
                break
            getattr(self,x)()


    def create_new_data(self):
        self.data = DAL.reading_csv_file()
        self.menu_new_model()


    def menu_new_model(self):

        Printer.menu_manager_model_traning()
        choice = input()
        x = MenuRouter.get_routes_manager_nemu_add_data(choice)
        if x:
            x(self)
        else:
            Printer.invalid_selection()

    def print_data_frame(self):
        print(self.data)

a = Manager()
a.start()
