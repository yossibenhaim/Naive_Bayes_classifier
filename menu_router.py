from DAL import DAL

class MenuRouter:
    routes = {
        "1": "1",
        "2": "2",
        "3": DAL.reading_csv_file,
    }

    @staticmethod
    def get_routes(choice):
        return MenuRouter.routes.get(choice)