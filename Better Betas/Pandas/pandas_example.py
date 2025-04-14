import pandas as pd
import numpy as np

# https://www.kaggle.com/datasets/iveeaten3223times/massive-yahoo-finance-dataset

def foo() -> pd.DataFrame:
    df:pd.DataFrame = pd.read_csv("../data/stock_details_5_years.csv")
    return df
    # result = df.groupby('A').agg({'B': 'mean'})  # Simple, but slow on large scale
