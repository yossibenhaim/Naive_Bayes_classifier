

class MenuRouter:
    routes = {
        "1": "1",
        "2": "2",
        "3": "3",
    }

    @staticmethod
    def get_routes(choice):
        return MenuRouter.routes.get(choice)