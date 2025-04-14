import pandas as pd
import numpy as np


def loading_dataset() -> pd.DataFrame:
    df:pd.DataFrame = pd.read_csv("../data/stock_details_5_years.csv")
    return df
    # result = df.groupby('A').agg({'B': 'mean'})  # Simple, but slow on large scale
