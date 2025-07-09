import pandas as pd

from printer import Printer


class DAL:


    @staticmethod
    def file_name_request():
        Printer.file_name_request()
        name_file = input()
        return fr"{name_file}"

    @staticmethod
    def reading_csv_file():
        name_file = DAL.file_name_request()
        date_frame = pd.read_csv(name_file)
        return date_frame