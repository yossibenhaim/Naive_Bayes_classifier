class Cleaning_data:

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def cleaning_data(self, name_column):
        data_frame = self.data_frame.set_index(name_column)
        print(data_frame)
        return data_frame




