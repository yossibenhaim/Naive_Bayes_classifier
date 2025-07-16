class Cleaning_data:

    def __init__(self, data_frame):
        """
        Initializes the cleaning class with a DataFrame.
        """
        self.data_frame = data_frame

    def cleaning_data(self, name_column):
        """
        Sets the given column as the index of the DataFrame.
        """
        data_frame = self.data_frame.set_index(name_column)
        return data_frame




