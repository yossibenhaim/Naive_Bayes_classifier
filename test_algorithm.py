import pandas as pd


class Algorithm:

    def __init__(self):
        self.count = 0
        self.count_true = 0


    def creat_list_of_dict(self, data):
        data = data.reset_index()
        df_without_id_Buy_Computer = data.drop(columns=["id", "Buy_Computer"])
        minus_data = df_without_id_Buy_Computer.to_dict(orient="records")
        return minus_data

    def creat_list_of_dict1(self, data):
        # data = data.set_index("Buy_Computer")
        minus_data = data.reset_index().to_dict(orient="records")
        return minus_data

