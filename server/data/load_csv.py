import pandas as pd
import requests
from io import StringIO
import json
import os
import logging

main_server_logger = logging.getLogger("main_server_logger")


class LoadCsv:

    def __init__(self):
        """
        Initializes loader with default filenames for CSV and probability JSON.
        """
        self._name_csv = "data.csv"
        self._name_probability_dict = "probability.json"
        self._storage_path = "data/storage/"
        main_server_logger.info(f"LoadCsv initialized with storage path: {self._storage_path}")

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
        main_server_logger.info(f"Loading CSV from URL: {url}")
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = pd.read_csv(StringIO(response.text))
                main_server_logger.info(f"CSV loaded successfully from {url}, shape: {data.shape}")
                return data
            except Exception as e:
                main_server_logger.error(f"Failed to parse CSV from {url}: {e}")
                raise ValueError(f"Failed to parse CSV: {e}")
        else:
            main_server_logger.error(f"Failed to load CSV from {url}, status code: {response.status_code}")
            raise ConnectionError(f"Failed to load CSV. Status code: {response.status_code}")

    def saving_data_csv(self, data):
        """
        Saves DataFrame to local CSV file.

        Args:
            data (pandas.DataFrame): Data to save.
        """
        try:
            path = os.path.join(self._storage_path, self._name_csv)
            data.to_csv(path)
            main_server_logger.info(f"Data saved to CSV at {path}")
        except Exception as e:
            main_server_logger.error(f"Failed to save CSV to {path}: {e}")
            raise

    def read_data_csv(self):
        """
        Reads saved CSV file as DataFrame.

        Returns:
            pandas.DataFrame: The data.
        """
        try:
            path = os.path.join(self._storage_path, self._name_csv)
            main_server_logger.info(f"Reading CSV from {path}")
            data = pd.read_csv(path, index_col=0)
            return data
        except Exception as e:
            main_server_logger.error(f"Failed to read CSV from {path}: {e}")
            raise

    def saving_probability(self, data):
        """
        Saves probability dictionary to JSON file.

        Args:
            data (dict): Probability data.
        """
        try:
            path = os.path.join(self._storage_path, self._name_probability_dict)
            with open(path, "w") as file:
                json.dump(data, file)
            main_server_logger.info(f"Probability data saved to JSON at {path}")
        except Exception as e:
            main_server_logger.error(f"Failed to save probability JSON to {path}: {e}")
            raise

    def read_probability_dict(self):
        """
        Reads probability dictionary from JSON file.

        Returns:
            dict: Probability data.
        """
        try:
            path = os.path.join(self._storage_path, self._name_probability_dict)
            main_server_logger.info(f"Reading probability data from JSON at {path}")
            with open(path, "r") as file:
                data = json.load(file)
            return data
        except Exception as e:
            main_server_logger.error(f"Failed to read probability JSON from {path}: {e}")
            raise
