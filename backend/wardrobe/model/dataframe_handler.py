import pandas as pd

class DataFrameHandler:
    def __init__(self, data=None):
        self.data = data

    def read_data(self):
        return self.data
    
    def write_to_df(self):
        df = pd.DataFrame.from_records(self.data, index={"name", "surname"})
        return df