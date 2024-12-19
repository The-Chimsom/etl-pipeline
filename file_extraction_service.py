import pandas as pd


class Extraction:
    def __init__(self, file_path):
        self.file_path= file_path
        self.data= self.load_csv()

    def load_csv(self):
        try:
           return pd.read_csv(self.file_path)
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return None