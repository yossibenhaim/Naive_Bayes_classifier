import pandas as pd
from Probability_Classifier import Probability
from Cleaning_data import Cleaning_data

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
