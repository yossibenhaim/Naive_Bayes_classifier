import pandas as pd
import requests
from io import StringIO
import json
import os


class LoadCsv:

    def __init__(self):
        """
        Initializes loader with default filenames for CSV and probability JSON.
        """
        self._name_csv = "data.csv"
        self._name_probability_dict = "probability.json"
        self._storage_path = r"C:\\Users\\user\\Desktop\\golen\\projects\\Naive_Bayes_classifier1\\server\\data\\storage\\"

    def load_csv(self, url):
        """
        Downloads and parses a CSV file from a URL.

        Args:
            url (str): URL of the CSV file.

        Returns:
            pandas.DataFrame: Parsed CSV data.

        Raises:
            ValueError: If CSV parsing fails.
            ConnectionError: If HTTP request fails.
        """
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = pd.read_csv(StringIO(response.text))
                return data
            except Exception as e:
                raise ValueError(f"Failed to parse CSV: {e}")
        else:
            raise ConnectionError(f"Failed to load CSV. Status code: {response.status_code}")

    def saving_data_csv(self, data):
        """
        Saves DataFrame to local CSV file.

        Args:
            data (pandas.DataFrame): Data to save.
        """
        data.to_csv(rf"{self._storage_path}{self._name_csv}")

    def read_data_csv(self):
        """
        Reads saved CSV file as DataFrame.

        Returns:
            pandas.DataFrame: The data.
        """
        print(os.path.abspath("storage/data.csv"))

        return pd.read_csv(fr"{self._storage_path}{self._name_csv}", index_col=0)

    def saving_probability(self, data):
        """
        Saves probability dictionary to JSON file.

        Args:
            data (dict): Probability data.
        """
        with open(fr"{self._storage_path}{self._name_probability_dict}", "w") as file:
            json.dump(data, file)

    def read_probability_dict(self):
        """
        Reads probability dictionary from JSON file.

        Returns:
            dict: Probability data.
        """
        with open(fr"{self._storage_path}{self._name_probability_dict}", "r") as file:
            data = json.load(file)
        return data
