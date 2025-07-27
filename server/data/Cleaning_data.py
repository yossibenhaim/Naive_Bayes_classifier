import logging

main_server_logger = logging.getLogger("main_server_logger")


class Cleaning_data:

    def __init__(self, data_frame):
        """
        Initializes with a pandas DataFrame.

        Args:
            data_frame (pandas.DataFrame): The DataFrame to clean.
        """
        self.data_frame = data_frame
        main_server_logger.info(f"Cleaning_data initialized with DataFrame shape: {data_frame.shape}")

    def cleaning_data(self, name_column):
        """
        Sets the specified column as the DataFrame's index.

        Args:
            name_column (str): The column name to set as index.

        Returns:
            pandas.DataFrame: DataFrame with new index set.

        Raises:
            KeyError: If the specified column does not exist.
        """
        try:
            data_frame = self.data_frame.set_index(name_column)
            main_server_logger.info(f"Set column '{name_column}' as DataFrame index.")
            return data_frame
        except KeyError:
            main_server_logger.error(f"Column '{name_column}' not found in DataFrame columns.")
            raise
