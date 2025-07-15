import pandas as pd
import requests
import logging

logging.basicConfig(level=logging.INFO, filename="logs/log.log", )
logger = logging.getLogger(__name__)


class Manager:

    def __init__(self):
        self._url = "http://127.0.0.1:8000"

    def load_csv_and_process(self):
        url = {"url" : input("send your a url")}
        response = requests.post(fr"{self._url}/csv/load", json=url)
        return response if response.status_code == 200 else "error:"



    def clean_data(self):
        name_column = {"column": self.choice_column()}
        response = requests.post(fr"{self._url}/csv/columns", json=name_column)
        return response if response.status_code == 200 else "error:"


    def create_probability(self):
        response = requests.post(fr"{self._url}/model/train")
        return response if response.status_code == 200 else "error:"

    def test_probability(self):
        response = requests.post(fr"{self._url}/model/test")
        print(response.json()["result"])
        return response if response.status_code == 200 else "error:"

    def check_probability(self):
        dict_row = {"row":self.create_dict_to_check()}
        response = requests.post(fr"{self._url}/model/check", json=dict_row)
        print(response.json()["result"])
        return response if response.status_code == 200 else "error:"


    def return_data_frame(self):
        response = requests.get(fr"{self._url}/csv/preview")
        if response.status_code == 200:
            dataframe = pd.DataFrame(response.json()["result"])
            dataframe = dataframe.set_index(response.json()["name_index"])
            return dataframe
        return None

    def create_dict_to_check(self):
        dataframe = self.return_data_frame()
        if dataframe is not None:
            dict_row = {}
            columns = dataframe.columns

            for column in columns:
                if column == "id":
                    continue
                unique_values = dataframe[column].unique()
                print(f"\n {column}: {list(unique_values)}")
                value = input(f" '{column}': ")
                dict_row[column] = value
            return dict_row
        else:
            return "error:"

    def choice_column(self):
        dataframe = self.return_data_frame()
        columns = dataframe.columns
        stop_loop = True
        while stop_loop:
            column = input(f"send your choice in {columns}")
            if column in columns:
                stop_loop = False
        return column

