import pandas as pd
from Probability_Classifier import Probability
from Cleaning_data import Cleaning_data
from Test_for_classifier import Test_classifier

class Manager:

    def __init__(self):
        self._data_frame = None
        self._data_probability = None
        self._class_probability = Probability()
        self._class_Clean_data = Cleaning_data()

    def load_csv(self):
        url = input("send url to load a csv")
        self._data_frame = pd.read_csv(r"C:\Users\user\Downloads\buy_computer.csv")

    def clean_data(self):
        self._data_frame = self._class_Clean_data.cleaning_data(self._data_frame)

    def create_probability(self):
        self._class_probability.create_probability(self._data_frame)

    def create_check_probability(self):
        test = Test_classifier(self._class_probability)
        dict_row = self.create_dict_to_check()
        result = test.check_probability(dict_row)
        print(f"\nPredicted class: {result}")

    def create_dict_to_check(self):
        if self._data_frame is None:
            print("Error:")
            return {}

        dict_row = {}
        columns = self._data_frame.columns

        for column in columns:
            if column == "id":
                continue
            unique_values = self._data_frame[column].unique()
            print(f"\n {column}: {list(unique_values)}")
            value = input(f" '{column}': ")
            dict_row[column] = value

        return dict_row


