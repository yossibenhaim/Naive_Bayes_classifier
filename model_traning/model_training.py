class ModelTraining:

    def __init__(self, data):
        self.data = data
        self.data_dict = {}
        index_value_counts = self.data.index.value_counts()
        for key in index_value_counts.index:
             self.data_dict[key] = {}

        for current in self.data_dict:
            for column in self.data:
                if column == "id":
                    continue
                if column not in self.data_dict[current]:
                    self.data_dict[current][column] = {}
                value_counts = self.data.loc[self.data.index == current, column].value_counts()
                for row, value in value_counts.items():
                    count_true = len(self.data[(self.data[column] == row) & (self.data.index == current)])
                    self.data_dict[current][column][row] = {"count": value, "is_true": count_true, "probability": 0}
                    probability = self.data_dict[current][column][row]["is_true"] / self.data_dict[current][column][row]["count"]
                    self.data_dict[current][column][row]["probability"] = probability