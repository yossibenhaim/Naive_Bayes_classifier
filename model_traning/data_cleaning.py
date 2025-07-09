import pandas as pd

class DataCleaning:

    def __init__(self, data):
        self.data = data

    def change_index(self):
        new_index = self.request_column_name()
        self.data.set_index(new_index, inplace=True)
        return self.data

    def request_column_name(self):
        return input("send your choice column")
