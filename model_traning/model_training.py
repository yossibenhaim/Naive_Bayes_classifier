from idlelib.debugobj_r import remote_object_tree_item

import pandas as pd
import numpy as np


class ModelTraining:

    def __init__(self, data):
        self.data = data
        index_value_counts = self.data.index.value_counts()
        self.data_dict = {index_value_counts.index[0]: {}, index_value_counts.index[1]: {}}


        for z in self.data_dict:
            for i in self.data:
                if i == "id":
                    continue
                if i in self.data_dict[z]:
                    pass
                else:
                    self.data_dict[z][i] = {}
                value_counts = self.data[[i]].value_counts()
                for x, v in value_counts.items():
                    self.data_dict[z][i][x[0]] = v

        for z in self.data_dict.keys():
            for i in self.data_dict[z]:
                for k, v in self.data_dict[z][i].items():
                    if not isinstance(self.data_dict[z][i][k], dict):
                        self.data_dict[z][i][k] = {"count": 0, "is_true": 0, "probability": 0}
                    self.data_dict[z][i][k]["count"] += v

        for z in self.data_dict.keys():
            for i, ii in self.data_dict[z].items():
                for k, v in self.data_dict[z][i].items():
                    self.data_dict[z][i][k]["is_true"] = len(self.data[(self.data[i] == k) & (self.data.index == z)])
                    self.data_dict[z][i][k]["probability"] = self.data_dict[z][i][k]["is_true"] / self.data_dict[z][i][k]["count"]

    # def return_data_dict(self):
    #     return self.data_dict