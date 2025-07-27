import logging

main_server_logger = logging.getLogger("main_server_logger")


class Probability:

    def __init__(self):
        """
        Initializes the Probability object with empty dataset and probability dictionary.
        """
        self._data_frame = None
        self._data_dict = {}
        main_server_logger.info("Probability instance created with empty data.")

    def create_probability(self, data):
        """
        Creates a probability dictionary from the given training data.

        Args:
            data (pandas.DataFrame): The training dataset with class labels as index.

        Returns:
            dict: A nested dictionary containing class-wise conditional probabilities.

        Raises:
            ValueError: If data is None or empty.
        """
        if data is None or data.empty:
            main_server_logger.error("Input data for create_probability is None or empty.")
            raise ValueError("Input data cannot be None or empty.")

        self._data_frame = data
        self._data_dict = {}

        try:
            self.create_dict_index()
            self.create_dict_columns()
            self.create_dict_values()
            main_server_logger.info("Probability dictionary created successfully.")
            main_server_logger.debug(f"Probability dictionary content: {self._data_dict}")
            return self._data_dict
        except Exception as e:
            main_server_logger.error(f"Error while creating probability dictionary: {e}")
            raise

    def create_dict_index(self):
        """
        Initializes the probability dictionary keys for each class label found in the DataFrame index.

        Raises:
            AttributeError: If self._data_frame is not set.
        """
        if self._data_frame is None:
            main_server_logger.error("Data frame is not initialized before create_dict_index.")
            raise AttributeError("Data frame is not initialized.")

        index_value_counts = self._data_frame.index.value_counts()
        for key in index_value_counts.index:
            self._data_dict[key] = {}
        main_server_logger.info(f"Initialized probability dictionary keys for classes: {list(self._data_dict.keys())}")

    def create_dict_columns(self):
        """
        Sets up sub-dictionaries for each feature column within each class in the probability dictionary.

        Skips columns named 'id'.
        """
        if self._data_dict is None or not self._data_dict:
            main_server_logger.error("Probability dictionary is empty before create_dict_columns.")
            raise ValueError("Probability dictionary must be initialized before setting columns.")

        for current_class in self._data_dict:
            for column in self._data_frame.columns:
                if column == "id":
                    continue
                if column not in self._data_dict[current_class]:
                    self._data_dict[current_class][column] = {}
        main_server_logger.info("Initialized sub-dictionaries for each column in each class.")

    def create_dict_values(self):
        """
        Computes conditional probabilities of each value in every column for each class
        and populates the probability dictionary accordingly.

        Skips columns named 'id'.
        """
        if self._data_dict is None or not self._data_dict:
            main_server_logger.error("Probability dictionary is empty before create_dict_values.")
            raise ValueError("Probability dictionary must be initialized before populating values.")

        try:
            for current_class in self._data_dict:
                for column in self._data_frame.columns:
                    if column == "id":
                        continue
                    value_counts = self._data_frame.loc[self._data_frame.index == current_class, column].value_counts()
                    count_all = len(self._data_frame[self._data_frame.index == current_class])
                    for value, count in value_counts.items():
                        self._data_dict[current_class][column][value] = {
                            "is_true": count,
                            "count all": count_all,
                            "probability": count / count_all
                        }
            main_server_logger.info("Calculated and stored conditional probabilities for all classes and columns.")
        except Exception as e:
            main_server_logger.error(f"Error while calculating conditional probabilities: {e}")
            raise
