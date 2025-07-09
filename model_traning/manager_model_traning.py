# from model_traning.DAL import DAL
# from printer import Printer
#
#
# class Manager_Model_Traning:
#
#     def __init__(self):
#         self.data = DAL.reading_csv_file()
#         self.menu_new_model()
#
#     def menu_new_model(self):
#         from menu_router import MenuRouter
#
#         Printer.menu_manager_model_traning()
#         choice = input()
#         x = MenuRouter.get_routes_manager_nemu_add_data(choice)
#         if x:
#             x(self)
#         else:
#             Printer.invalid_selection()
#
#     def print_data_frame(self):
#         print(self.data)