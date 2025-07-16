class Cleaning_data:

    def __init__(self, data_frame):
        """
        Initializes with a pandas DataFrame.

        Args:
            data_frame (pandas.DataFrame): The DataFrame to clean.
        """
        self.data_frame = data_frame

    def cleaning_data(self, name_column):
        """
        Sets the specified column as the DataFrame's index.

        Args:
            name_column (str): The column name to set as index.

        Returns:
            pandas.DataFrame: DataFrame with new index set.
        """
        data_frame = self.data_frame.set_index(name_column)
        return data_frame




