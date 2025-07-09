import pandas as pd

class DataCleaning:

    def __init__(self, data):
        self.data = data

    def change_index(self, new_index):
        self.data.set_index(new_index)
