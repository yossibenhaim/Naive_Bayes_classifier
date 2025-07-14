import pandas as pd
import json

class LoadCsv:

    def __init__(self):
        self._name_csv = "data.csv"
        self._name_probability_dict = "probability.json"

    def load_csv(self, url):
        return pd.read_csv(fr"{url}")

    def saving_data_csv(self, data):
        data.to_csv(self._name_csv)

    def read_data_csv(self):
        return pd.read_csv(self._name_csv, index_col=0)

    def saving_probability(self, data):
        with open(self._name_probability_dict,"w") as file:
            json.dump(data, file)

    def read_probability_dict(self):
        with open(self._name_probability_dict,"r") as file:
            data = json.load(file)
        return data