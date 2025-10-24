import pandas as pd

def get_moisture_data():
    """Reading the last moisture data from CSV file"""
    df = pd.read_csv("moisture.csv")
    last_row = df.iloc[-1]
    return int(last_row["moisture"])
