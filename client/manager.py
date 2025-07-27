import pandas as pd
import requests
import os
import logging

os.makedirs("logs", exist_ok=True)

client_logger = logging.getLogger("client_logger")
client_logger.setLevel(logging.INFO)
fh = logging.FileHandler("logs/client.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
client_logger.addHandler(fh)

client_logger.info("Client started.")


class Manager:

    def __init__(self):
        """
        Initialize Manager with base URLs for API endpoints.
        """
        self._url = "http://127.0.0.1:8000"
        self._url_classifier = "http://127.0.0.1:8001"
        client_logger.info("Manager initialized with base URLs.")

    def load_csv_and_process(self):
        """
        Ask user for CSV URL, send to server to load and save locally,
        then clean data, train and test the model.

        Returns:
            requests.Response or str: Server response or "error:" on failure.
        """
        try:
            url = {"url": input("Send your CSV URL: ")}
            client_logger.info(f"Loading CSV from URL: {url['url']}")
            response = requests.post(f"{self._url}/csv/load", json=url, timeout=10)
            response.raise_for_status()

            self.clean_data()
            self.create_probability()
            self.test_probability()

            client_logger.info("CSV loaded and processed successfully.")
            return response

        except requests.exceptions.RequestException as e:
            client_logger.error(f"Failed to load CSV and process: {e}")
            return "error:"

    def clean_data(self):
        """
        Ask user to select a column to set as DataFrame index, send choice to server.

        Returns:
            requests.Response or str: Server response or "error:" on failure.
        """
        try:
            column_choice = self.choice_column()
            client_logger.info(f"Selected index column: {column_choice}")
            name_column = {"column": column_choice}
            response = requests.post(f"{self._url}/csv/columns", json=name_column, timeout=10)
            response.raise_for_status()
            client_logger.info("Index column set successfully.")
            return response

        except requests.exceptions.RequestException as e:
            client_logger.error(f"Failed to set index column: {e}")
            return "error:"

    def create_probability(self):
        """
        Trigger training of the Naive Bayes model on the server.

        Returns:
            requests.Response or str: Server response or "error:" on failure.
        """
        try:
            response = requests.post(f"{self._url}/model/train", timeout=10)
            response.raise_for_status()
            client_logger.info("Model training completed successfully.")
            return response

        except requests.exceptions.RequestException as e:
            client_logger.error(f"Model training failed: {e}")
            return "error:"

    def test_probability(self):
        """
        Trigger testing of the trained model and print accuracy results.

        Returns:
            requests.Response or str: Server response or "error:" on failure.
        """
        try:
            response = requests.post(f"{self._url}/model/test", timeout=100)
            response.raise_for_status()
            result = response.json().get("result", None)
            if result is not None:
                print(result)
                client_logger.info(f"Model test result: {result}")
            else:
                client_logger.warning("Test response missing 'result' key.")
            return response

        except requests.exceptions.RequestException as e:
            client_logger.error(f"Model testing failed: {e}")
        except ValueError:
            client_logger.error("Invalid JSON received during model testing.")
        return "error:"

    def check_probability(self):
        """
        Prompt user for new input row, send it for classification, and print results.

        Returns:
            requests.Response or str: Server response or "error:" on failure.
        """
        try:
            dict_row = self.create_dict_to_check()
            if dict_row == "error:":
                client_logger.error("No data available to create input row for classification.")
                return "error:"
            response = requests.post(f"{self._url_classifier}/model/check", json={"row": dict_row}, timeout=10)
            response.raise_for_status()
            result = response.json().get("result", None)
            if result:
                self.print_result_of_classifier(result)
                client_logger.info("Classification performed successfully.")
            else:
                client_logger.warning("Classification response missing 'result' key.")
            return response

        except requests.exceptions.RequestException as e:
            client_logger.error(f"Probability check request failed: {e}")
        except ValueError:
            client_logger.error("Invalid JSON received from classifier.")
        return "error:"

    def return_data_frame(self):
        """
        Retrieve the current dataset from the server as a pandas DataFrame.

        Returns:
            pandas.DataFrame or None: The dataset or None if retrieval failed.
        """
        try:
            response = requests.get(f"{self._url}/csv/preview", timeout=10)
            response.raise_for_status()
            data = response.json()
            dataframe = pd.DataFrame(data["result"])
            name_index = data.get("name_index", None)
            if name_index and name_index in dataframe.columns:
                dataframe = dataframe.set_index(name_index)
            client_logger.info("DataFrame retrieved successfully.")
            return dataframe

        except requests.exceptions.RequestException as e:
            client_logger.error(f"Failed to retrieve DataFrame: {e}")
        except (ValueError, KeyError) as e:
            client_logger.error(f"Invalid or incomplete JSON data received: {e}")
        return None

    def create_dict_to_check(self):
        """
        Prompt user to enter values for each column to form an input row for classification.

        Returns:
            dict or str: Dictionary of input values or "error:" if data unavailable.
        """
        dataframe = self.return_data_frame()
        if dataframe is None:
            client_logger.error("DataFrame is unavailable for input creation.")
            return "error:"

        dict_row = {}
        for column in dataframe.columns:
            if column.lower() in ("id", "index"):
                continue
            unique_values = dataframe[column].unique()
            print(f"\n{column}: {list(unique_values)}")
            value = input(f"Enter value for '{column}': ")
            dict_row[column] = value
        client_logger.info(f"Input row created for classification: {dict_row}")
        return dict_row

    def choice_column(self):
        """
        Prompt user to select a valid column name to be used as index.

        Returns:
            str: Selected column name.
        """
        dataframe = self.return_data_frame()
        if dataframe is None:
            client_logger.error("DataFrame unavailable for choosing index column.")
            return ""
        columns = dataframe.columns.tolist()

        while True:
            column = input(f"Choose index column from {columns}: ")
            if column in columns:
                client_logger.info(f"User selected index column: {column}")
                return column
            print("Invalid column name. Please try again.")

    def print_result_of_classifier(self, result):
        """
        Print the classification probabilities and highlight the highest probability.

        Args:
            result (dict): Mapping of class labels to probabilities.
        """
        for key, value in result.items():
            print(f"The probability of class '{key}' is {value}")
        highest = max(result, key=result.get)
        print(f"The highest probability is for class: {highest}")
        client_logger.info(f"Classification results printed: highest class '{highest}'")
