import pandas as pd
import numpy as np

def extract_data(file_name):

    df = pd.read_excel(file_name)
    if df is None:
        print("nothing to see")

    return df
