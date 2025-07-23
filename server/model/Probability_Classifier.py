class Probability:

    def __init__(self):
        """
        Initializes with empty data.
        """
        self._data_frame = None
        self._data_dict = {}

    def create_probability(self, data):
        """
        Creates probability dictionary based on data.

        Args:
            data (pandas.DataFrame): The training data.

        Returns:
            dict: Probability dictionary with class and feature probabilities.
        """
        self._data_frame = data
        self._data_dict = {}
        self.create_dict_index()
        self.create_dict_columns()
        self.create_dict_values()
        print(self._data_dict)
        return self._data_dict

    def create_dict_index(self):
        """
        Initializes dictionary keys for each class label from index values.
        """
        index_value_counts = self._data_frame.index.value_counts()
        for key in index_value_counts.index:
            self._data_dict[key] = {}

    def create_dict_columns(self):
        """
        Initializes sub-dictionaries for each column in each class.
        """
        for current in self._data_dict:
            for column in self._data_frame:
                if column == "id":
                    continue
                if column not in self._data_dict[current]:
                    self._data_dict[current][column] = {}

    def create_dict_values(self):
        """
        Calculates conditional probabilities for values in each column per class.
        """
        for current in self._data_dict:
            for column in self._data_frame:
                if column == "id":
                    continue
                value_counts = self._data_frame.loc[self._data_frame.index == current, column].value_counts()
                for row, value in value_counts.items():
                    count_all = len(self._data_frame[self._data_frame.index == current])
                    self._data_dict[current][column][row] = {
                        "is_true": value,
                        "count all": count_all,
                        "probability": value / count_all
                    }
