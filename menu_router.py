from model_traning.manager_model_traning import Manager_Model_Traning

class MenuRouter:
    routes_start_nemu = {
        "1": "1",
        "2": "2",
        "3": Manager_Model_Traning,
    }
    routes_manager_nemu_add_data = {
        "1": Manager_Model_Traning.print_data_frame,
        "2": "2",
        "3": "exit",
    }


    @staticmethod
    def get_routes_start_nemu(choice):
        return MenuRouter.routes_start_nemu.get(choice)

    @staticmethod
    def get_routes_manager_nemu_add_data(choice):
        return MenuRouter.routes_manager_nemu_add_data.get(choice)