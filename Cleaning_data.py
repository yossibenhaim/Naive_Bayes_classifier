class Cleaning_data:

    def __int__(self):
        self.data_frame = None

    def cleaning_data(self, data):
        self.data_frame = data
        self.data_frame = self.data_frame.set_index(self.choice_column())
        return self.data_frame



    def choice_column(self):
        columns = self.data_frame.columns
        stop_loop = True
        while stop_loop:
            column = input(f"send your choice in {columns}")
            if column in columns:
                stop_loop = False
        return column
