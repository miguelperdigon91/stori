import pandas as pd


class CSVReader:
    @staticmethod
    def read(path_file: str):
        data = pd.read_csv(path_file)

        return data
