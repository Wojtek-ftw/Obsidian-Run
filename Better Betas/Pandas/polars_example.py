import polars as pl

def foo():
    df = pl.read_csv("../data/stock_details_5_years.csv", infer_schema_length=None)
    return df
