import pandas as pd
from Probability_Classifier import Probability

class manager:

    def __init__(self):
        self._data_frame = None
        self._data_probability = None
        self._class_probability = Probability()

    def load_csv(self):
        url = input("send url to load a csv")
        self._data_frame = pd.read_csv(url)

    def create_probability(self):
        self._class_probability.create_probability(self._data_frame)


