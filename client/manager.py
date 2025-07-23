import pandas as pd
import requests


# import logging
#
# logging.basicConfig(level=logging.INFO, filename="logs/log.log", )
# logger = logging.getLogger(__name__)

class Manager:

    def __init__(self):
        """
        Initializes the Manager with the base URL of the local API.
        """
        self._url = "http://127.0.0.1:8000"
        self._url_classifier = "http://127.0.0.1:8001"

    def load_csv_and_process(self):
        """
        Prompts the user for a CSV URL and sends it to the server to load and save locally.

        Returns:
            requests.Response | str: The response from the server or "error:" on failure.
        """
        url = {"url": input("send your a url")}
        response = requests.post(fr"{self._url}/csv/load", json=url)
        return response if response.status_code == 200 else "error:"

    def clean_data(self):
        """
        Prompts the user to choose a column to use as index and sends it to the server.

        Returns:
            requests.Response | str: The response from the server or "error:" on failure.
        """
        name_column = {"column": self.choice_column()}
        response = requests.post(fr"{self._url}/csv/columns", json=name_column)
        return response if response.status_code == 200 else "error:"

    def create_probability(self):
        """
        Sends a request to train the Naive Bayes model.

        Returns:
            requests.Response | str: The response from the server or "error:" on failure.
        """
        response = requests.post(fr"{self._url}/model/train")
        return response if response.status_code == 200 else "error:"

    def test_probability(self):
        """
        Sends a request to evaluate the model accuracy.

        Returns:
            requests.Response | str: The response from the server or "error:" on failure.
        """
        response = requests.post(fr"{self._url}/model/test")
        print(response.json()["result"])
        return response if response.status_code == 200 else "error:"

    def check_probability(self):
        """
        Prompts the user to input a new row and checks the predicted class.

        Returns:
            requests.Response | str: The response from the server or "error:" on failure.
        """
        dict_row = self.create_dict_to_check()
        response = requests.post(fr"{self._url_classifier}/model/check", json={"row": dict_row})
        self.print_result_of_classifier(response.json()["result"])
        return response if response.status_code == 200 else "error:"

    def return_data_frame(self):
        """
        Gets the current dataset from the server and returns it as a pandas DataFrame.

        Returns:
            pandas.DataFrame | None: The current DataFrame, or None if the request failed.
        """
        response = requests.get(fr"{self._url}/csv/preview")
        if response.status_code == 200:
            dataframe = pd.DataFrame(response.json()["result"])
            name_index = response.json()["name_index"]
            if name_index in dataframe.columns:
                dataframe = dataframe.set_index(response.json()["name_index"])
            return dataframe
        return None

    def create_dict_to_check(self):
        """
        Prompts the user to enter values for each column to create a test input.

        Returns:
            dict | str: A dictionary of user input values or "error:" if DataFrame is unavailable.
        """
        dataframe = self.return_data_frame()
        if dataframe is not None:
            dict_row = {}
            columns = dataframe.columns
            for column in columns:
                if column in ("id", "index", "Index"):
                    continue
                unique_values = dataframe[column].unique()
                print(f"\n {column}: {list(unique_values)}")
                value = input(f" '{column}': ")
                dict_row[column] = value
            return dict_row
        else:
            return "error:"

    def choice_column(self):
        """
        Prompts the user to choose one of the dataset's columns to be used as index.

        Returns:
            str: The chosen column name.
        """
        dataframe = self.return_data_frame()
        columns = dataframe.columns
        stop_loop = True
        while stop_loop:
            column = input(f"send your choice in {columns}")
            if column in columns:
                stop_loop = False
        return column

    def print_result_of_classifier(self, result):
        for key, value in result.items():
            print(f"teh probability of index {key} == {value}")
        print(f"the big probability in {max(result, key=result.get)}")
