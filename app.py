import pandas as pd
import numpy as np

def load_df():
    return pd.read_csv('data/raw/bike.csv')

if __name__ == '__main__':
    df = load_df()

